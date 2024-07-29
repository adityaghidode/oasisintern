import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pickle
import os

class EnhancedBMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced BMI Calculator")

        self.users_data = self.load_data()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.root, text="Weight (kg)").grid(row=1, column=0)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=1, column=1)

        tk.Label(self.root, text="Height (m)").grid(row=2, column=0)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=2, column=1)

        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi).grid(row=3, columnspan=2)

        self.label_bmi = tk.Label(self.root, text="BMI: ")
        self.label_bmi.grid(row=4, columnspan=2)

        tk.Button(self.root, text="Show BMI Graph", command=self.show_bmi_graph).grid(row=5, columnspan=2)

    def calculate_bmi(self):
        name = self.entry_name.get()
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height")
            return

        bmi = weight / (height ** 2)
        self.label_bmi.config(text=f"BMI: {bmi:.2f}")

        if name not in self.users_data:
            self.users_data[name] = []
        self.users_data[name].append(bmi)

        self.save_data()

    def save_data(self):
        with open('bmi_data.pkl', 'wb') as f:
            pickle.dump(self.users_data, f)

    def load_data(self):
        if os.path.exists('bmi_data.pkl'):
            with open('bmi_data.pkl', 'rb') as f:
                return pickle.load(f)
        return {}

    def show_bmi_graph(self):
        if not self.users_data:
            messagebox.showinfo("No data", "No BMI data available")
            return

        plt.figure(figsize=(10, 6))

        for name, bmis in self.users_data.items():
            plt.plot(bmis, marker='o', label=name)

        plt.xlabel('Entries')
        plt.ylabel('BMI')
        plt.title('BMI History for All Students')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedBMICalculator(root)
    root.mainloop()
