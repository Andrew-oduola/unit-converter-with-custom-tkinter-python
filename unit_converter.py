import tkinter as tk
import customtkinter as ctk


class WeightConverter:
    @staticmethod
    def grams_to_kilograms(grams):
        return grams / 1000
    
    @staticmethod
    def kilograms_to_grams(kilograms):
        return kilograms * 1000
    
    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * 2.20462
    
    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds / 2.20462
    
    @staticmethod
    def grams_to_ounces(grams):
        return grams / 28.3495
    
    @staticmethod
    def ounces_to_grams(ounces):
        return ounces * 28.3495
    
    @staticmethod
    def pounds_to_ounces(pounds):
        return pounds * 16
    
    @staticmethod
    def ounces_to_pounds(ounces):
        return ounces / 16



class LengthConverter:
    @staticmethod
    def meters_to_kilometers(meters):
        return meters / 1000
    
    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers / 1000
    
    @staticmethod
    def meters_to_centimeters(meters):
        return meters * 100
    
    @staticmethod
    def centimeters_to_meters(centimeters):
        return centimeters / 100
    
    @staticmethod
    def meters_to_miles(meters):
        return meters / 1609.344
    
    @staticmethod
    def miles_to_meters(miles):
        return miles * 1609.344
    
    @staticmethod
    def meters_to_yards(meters):
        return meters * 1.09361
    
    @staticmethod
    def yards_to_meters(yards):
        return yards / 1.09361
    
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    
    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084
    
    @staticmethod
    def meters_to_inches(meters):
        return meters * 39.3701
    
    @staticmethod
    def inches_to_meters(inches):
        return inches / 39.3701
    
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return (celsius + 273.15)
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return (kelvin - 273.15)
    
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin * 9/5) - 459.67
    
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit + 459.67) * 5/9
    

class Main:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.root.geometry("600x300")
        self.root.title("Unit Converter")
        self.create_ui()

    def create_ui(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tab_control = ctk.CTkTabview(self.main_frame)
        self.weight_tab = self.tab_control.add('Weight')
        self.length_tab = self.tab_control.add('Length')
        self.temperature_tab = self.tab_control.add('Temperature')

        self.tab_control.pack(expand=True, fill=tk.BOTH)

        self.create_weight_tab()
        self.create_length_tab()
        self.create_temperature_tab()


    def create_weight_tab(self):
        self.VAL_WEIGHT = ['Grams', 'Kilograms', 'Pounds', 'Ounces']
        self.UNIT_WEIGHT_1 = tk.StringVar(value=self.VAL_WEIGHT[0])
        self.UNIT_WEIGHT_2 = tk.StringVar(value=self.VAL_WEIGHT[1])
        self.VALUE_WEIGHT = tk.StringVar()
        self.RESULT_WEIGHT = tk.StringVar()

        weight_label = ctk.CTkLabel(self.weight_tab, text='Weight Conversion', font=("Helvetica", 16, "bold"))
        weight_label.pack(pady=10)

        weight_frame = ctk.CTkFrame(self.weight_tab)
        weight_frame.pack(fill=tk.X, pady=10)

        self.create_conversion_ui(weight_frame, self.VAL_WEIGHT, self.UNIT_WEIGHT_1, self.UNIT_WEIGHT_2, self.VALUE_WEIGHT, self.RESULT_WEIGHT, self.convert_weight)

    def create_length_tab(self):
        self.VAL_LENGTH = ['Meters', 'Kilometers', 'Centimeters', 'Miles', 'Yards', 'Feet', 'Inches']
        self.UNIT_LENGTH_1 = tk.StringVar(value=self.VAL_LENGTH[0])
        self.UNIT_LENGTH_2 = tk.StringVar(value=self.VAL_LENGTH[1])
        self.VALUE_LENGTH = tk.StringVar()
        self.RESULT_LENGTH = tk.StringVar()

        length_label = ctk.CTkLabel(self.length_tab, text='Length Conversion', font=("Helvetica", 16, "bold"))
        length_label.pack(pady=10)

        length_frame = ctk.CTkFrame(self.length_tab)
        length_frame.pack(fill=tk.X, pady=10)

        self.create_conversion_ui(length_frame, self.VAL_LENGTH, self.UNIT_LENGTH_1, self.UNIT_LENGTH_2, self.VALUE_LENGTH, self.RESULT_LENGTH, self.convert_length)

    def create_temperature_tab(self):
        self.VAL_TEMPERATURE = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.UNIT_TEMPERATURE_1 = tk.StringVar(value=self.VAL_TEMPERATURE[0])
        self.UNIT_TEMPERATURE_2 = tk.StringVar(value=self.VAL_TEMPERATURE[1])
        self.VALUE_TEMPERATURE = tk.StringVar()
        self.RESULT_TEMPERATURE = tk.StringVar()

        temperature_label = ctk.CTkLabel(self.temperature_tab, text='Temperature Conversion', font=("Helvetica", 16, "bold"))
        temperature_label.pack(pady=10)
        temperature_frame = ctk.CTkFrame(self.temperature_tab)
        temperature_frame.pack(fill=tk.X, pady=10)

        self.create_conversion_ui(temperature_frame, self.VAL_TEMPERATURE, self.UNIT_TEMPERATURE_1, self.UNIT_TEMPERATURE_2, self.VALUE_TEMPERATURE, self.RESULT_TEMPERATURE, self.convert_temperature)


    def create_conversion_ui(self, frame, unit_options, unit_var1, unit_var2, value_var, result_var, command_func=None):
        ctk.CTkLabel(frame, text='From:', font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        unit_box1 = ctk.CTkComboBox(frame, values=unit_options, variable=unit_var1, width=150)
        unit_box1.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text='To:', font=("Helvetica", 14)).grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        unit_box1 = ctk.CTkComboBox(frame, values=unit_options, variable=unit_var2, width=150)
        unit_box1.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Value:", font=("Helvetica", 14)).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ctk.CTkEntry(frame, textvariable=value_var, width=150).grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Result:", font=("Helvetica", 14)).grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        ctk.CTkEntry(frame, textvariable=result_var, state='readonly', width=150).grid(row=1, column=3, padx=10, pady=5)

        ctk.CTkButton(frame, text='Convert', command=command_func).grid(row=2, column=0, columnspan=4, pady=15)

    def convert_weight(self):
        unit_from = self.UNIT_WEIGHT_1.get()
        unit_to = self.UNIT_WEIGHT_2.get()
        value = self.VALUE_WEIGHT.get()
        if not value:
            self.RESULT_WEIGHT.set("Error")
            return
        
        try:
            value = float(value)
        except ValueError:
            self.RESULT_WEIGHT.set("Error")
            return
        
        result = None
        if unit_from == 'Grams' and unit_to == 'Kilograms':
            result = WeightConverter.grams_to_kilograms(value)
        elif unit_from == 'Kilograms' and unit_to == 'Grams':
            result = WeightConverter.kilograms_to_grams(value)
        elif unit_from == 'Kilograms' and unit_to == 'Grams':
            result = WeightConverter.kilograms_to_grams(value)

        elif unit_from == 'Kilograms' and unit_to == 'Pounds':
            result = WeightConverter.kilograms_to_pounds(value)
        elif unit_from == 'Pounds' and unit_to == 'Kilograms':
            result = WeightConverter.pounds_to_kilograms(value)

        elif unit_from == 'Grams' and unit_to == 'Ounces':
            result = WeightConverter.grams_to_ounces(value)
        elif unit_from == 'Ounces' and unit_to == 'Grams':
            result = WeightConverter.ounces_to_grams(value)
        elif unit_from == 'Pounds' and unit_to == 'Ounces':
            result = WeightConverter.pounds_to_ounces(value)
        elif unit_from == 'Ounces' and unit_to == 'Pounds':
            result = WeightConverter.ounces_to_pounds(value)
        else:
            self.RESULT_WEIGHT.set("Error")
            return
        
        self.RESULT_WEIGHT.set(f"{result:.4f}")

    def convert_length(self):
        unit_from = self.UNIT_LENGTH_1.get()
        unit_to = self.UNIT_LENGTH_2.get()
        value = self.VALUE_LENGTH.get()
        if not value:
            self.RESULT_LENGTH.set("Error")
            return
        
        try:
            value = float(value)
        except ValueError:
            self.RESULT_LENGTH.set("Error")
            return
        
        result = None

        if unit_from == "Meters"  and unit_to == "Kilometers":
            result = LengthConverter.meters_to_kilometers(value)
        elif unit_from == "Kilometers"  and unit_to == "Meters":
            result = LengthConverter.kilometers_to_meters(value)
        elif unit_from == "Meters"  and unit_to == "Centimeters":
            result = LengthConverter.meters_to_centimeters(value)
        elif unit_from == "Centimeters"  and unit_to == "Meters":
            result = LengthConverter.centimeters_to_meters(value)
        elif unit_from == "Meters"  and unit_to == "Miles":
            result = LengthConverter.meters_to_miles(value)
        elif unit_from == "Miles"  and unit_to == "Meters":
            result = LengthConverter.miles_to_meters(value)
        elif unit_from == "Meters"  and unit_to == "Yards":
            result = LengthConverter.meters_to_yards(value)
        elif unit_from == "Yards"  and unit_to == "Meters":
            result = LengthConverter.yards_to_meters(value)
        elif unit_from == "Meters"  and unit_to == "Feet":
            result = LengthConverter.meters_to_feet(value)
        elif unit_from == "Feet"  and unit_to == "Meters":
            result = LengthConverter.feet_to_meters(value)
        elif unit_from == "Meters"  and unit_to == "Inches":
            result = LengthConverter.meters_to_inches(value)
        elif unit_from == "Inches"  and unit_to == "Meters":
            result = LengthConverter.inches_to_meters(value)
        else:
            self.RESULT_LENGTH.set("Error")
            return
        
        self.RESULT_LENGTH.set(f"{result:.4f}")

    def convert_temperature(self):
        unit_from = self.UNIT_TEMPERATURE_1.get()
        unit_to = self.UNIT_TEMPERATURE_2.get()
        value = self.VALUE_TEMPERATURE.get()
        if not value:
            self.RESULT_TEMPERATURE.set("Error")
            return
        
        try:
            value = float(value)
        except ValueError:
            self.RESULT_TEMPERATURE.set("Error")
            return
        
        result = None

        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            result = TemperatureConverter.celsius_to_fahrenheit(value)
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            result = TemperatureConverter.fahrenheit_to_celsius(value)
        elif unit_from == "Celsius" and unit_to == "Kelvin":
            result = TemperatureConverter.celsius_to_kelvin(value)
        elif unit_from == "Kelvin" and unit_to == "Celsius":
            result = TemperatureConverter.kelvin_to_celsius(value)
        elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
            result = TemperatureConverter.celsius_to_fahrenheit(value)
        elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
            result = TemperatureConverter.celsius_to_fahrenheit(value)
        else:
            self.RESULT_TEMPERATURE.set("Error")
            return
        
        self.RESULT_TEMPERATURE.set(f"{result:.2f}")

root = tk.Tk()
app = Main(root)
root.mainloop()

