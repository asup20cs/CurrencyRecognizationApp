import tkinter as tk
from tkinter import filedialog
from camera import start_camera_capture
from convert import convert_currency
from PIL import ImageTk, Image
from tkinter import filedialog
#from predict import predict_image
from predict import predict_indian, predict_nepali
global image_path

def get_country():
    return country.get()

# Function to predict currency
def predict_currency(image_path):
    #predicted_currency = predict_image(image_path)
    #var_country.set(country.get())
    #var_denomination.set(predicted_currency)
    #return predicted_currency
    if country.get()=="India":
        predicted_currency = predict_indian(image_path)
        var_country.set(country.get())
        var_denomination.set(predicted_currency)
        return predicted_currency
    else:
        predicted_currency = predict_nepali(image_path)
        var_country.set(country.get())
        var_denomination.set(predicted_currency)
        return predicted_currency
       
# Function to handle browse image button click
def browse_image(image_label):
    try:
        # Open a file dialog for image selection
        image_path = filedialog.askopenfilename(
            initialdir="/",  # Adjust initial directory if needed
            title="Select Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]  # Filter for image formats
        )

        # Check if a file was selected
        if image_path:
            # Load the image using PIL
            image = Image.open(image_path)
            image = image.resize((432, 512))

            # Convert to a Tkinter-compatible format (optional, but recommended)
            image = image.convert("P")  # Convert to indexed palette (PNG format)

            # Create a Tkinter-compatible image object
            tk_image = ImageTk.PhotoImage(image)

            # Update the label with the new image
            image_label.config(image=tk_image)
            image_label.image = tk_image  # Keep a reference
            returned=predict_currency(image_path)
            convert(returned)
            
    except (OSError, FileNotFoundError) as e:
        print(f"Error: {e}")  # More specific error handling if needed

    except (Image.DecompressionBombError, Image.UnidentifiedImageError):
        print("Error: Invalid image format or corrupted file.")


# Function to handle start camera button click (placeholder for future implementation)
def start_camera():
  start_camera_capture()

  # Get the captured image path (assuming it's saved in the same directory)
  image_path = "captured_image.jpg"  # Replace with actual filename logic
  var_image_path.set(image_path)
  image = Image.open(image_path)
  image = image.resize((432, 512))
  image = image.convert("P")  # Convert to indexed palette (PNG format)

            # Create a Tkinter-compatible image object
  tk_image = ImageTk.PhotoImage(image)

            # Update the label with the new image
  image_label.config(image=tk_image)
  image_label.image = tk_image  # Keep a reference
  convert(predict_currency(image_path))

# Main application window
root = tk.Tk()
root.title("Currency Detection")
root.geometry("800x530")  # Set window size

# Image path variable (not writable)
image_path = ""
var_image_path = tk.StringVar(root, value=image_path)

# Container for components (frame)
component_frame = tk.Frame(root)
component_frame.pack(side="left", fill="both", expand=True)

# Container for image display (frame)
image_frame = tk.Frame(root)
image_frame.pack(side="right", fill="both", expand=True)

# Buttons (grid layout within component frame)
button_frame = tk.Frame(component_frame)  # Create a sub-frame for buttons
button_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E,columnspan=2)  # Place in grid

country=tk.StringVar()
def set_Country(selection):
   global country
   country.set(selection)
option_frame=tk.Frame(component_frame)
option_frame.grid(row=0, column=0, padx=10, pady=10,sticky=tk.W+tk.E)
option_label=tk.Label(option_frame, text="Choose country:")
option_label.pack(side="left", padx=5, pady=5)
countries = ["India", "Nepal"]
dropdown = tk.OptionMenu(option_frame, country, *countries,command=set_Country)
dropdown.config(width=10)
dropdown.pack()

browse_button = tk.Button(button_frame, text="Browse Image", command=lambda: browse_image(image_label))
browse_button.pack(side="left", padx=5, pady=5)  # Pack within sub-frame

start_camera_button = tk.Button(button_frame, text="Start Camera", command=start_camera)
start_camera_button.pack(side="right", padx=5, pady=5)  # Pack within sub-frame

# Labels and data holders (not writable) within component frame
country_label = tk.Label(component_frame, text="Country:")
country_label.grid(row=2, column=0, sticky="W")  # Use grid layout

var_country = country  # No writable argument needed
country_data = tk.Entry(component_frame, textvariable=var_country, state="disabled")
country_data.grid(row=2, column=1, padx=5, pady=5, sticky="EW")  # Add padding

denomination_label = tk.Label(component_frame, text="Denomination:")
denomination_label.grid(row=3, column=0, sticky="W")

var_denomination = tk.StringVar(root)  # No writable argument needed
denomination_data = tk.Entry(component_frame, textvariable=var_denomination, state="disabled")
denomination_data.grid(row=3, column=1, padx=5, pady=5, sticky="EW")

exchange_label= tk.Label(component_frame, text="Exchange Rates:")
exchange_label.grid(row=4, column=0, sticky="W")

#individual currency labels
usd_label = tk.Label(component_frame, text="USD:")
usd_label.grid(row=5, column=0, sticky="W")
var_usd = tk.StringVar(root)  # No writable argument needed
usd_data = tk.Entry(component_frame, textvariable=var_usd, state="disabled")
usd_data.grid(row=5, column=1, padx=5, pady=5, sticky="EW")

eur_label = tk.Label(component_frame, text="EUR:")
eur_label.grid(row=6, column=0, sticky="W")
var_eur = tk.StringVar(root)  # No writable argument needed
eur_data = tk.Entry(component_frame, textvariable=var_eur, state="disabled")
eur_data.grid(row=6, column=1, padx=5, pady=5, sticky="EW")

gbp_label = tk.Label(component_frame, text="GBP:")
gbp_label.grid(row=7, column=0, sticky="W")
var_gbp = tk.StringVar(root)  # No writable argument needed
gbp_data = tk.Entry(component_frame, textvariable=var_gbp, state="disabled")
gbp_data.grid(row=7, column=1, padx=5, pady=5, sticky="EW")

jpy_label = tk.Label(component_frame, text="JPY:")
jpy_label.grid(row=8, column=0, sticky="W")
var_jpy = tk.StringVar(root)  # No writable argument needed
jpy_data = tk.Entry(component_frame, textvariable=var_jpy, state="disabled")
jpy_data.grid(row=8, column=1, padx=5, pady=5, sticky="EW")

cny_label = tk.Label(component_frame, text="CNY:")
cny_label.grid(row=9, column=0, sticky="W")
var_cny = tk.StringVar(root)  # No writable argument needed
cny_data = tk.Entry(component_frame, textvariable=var_cny, state="disabled")
cny_data.grid(row=9, column=1, padx=5, pady=5, sticky="EW")

#function to convert currency
def convert(returned):
  amount = returned

  if country == "India":
    from_currency = 'INR'
  else:
    from_currency = 'NRS'
  to_currency = ['USD', 'EUR', 'GBP', 'JPY', 'CNY']
  converted_amount = []
  for currency in to_currency:
    converted_amount.append(convert_currency(amount, from_currency, currency))
  var_usd.set(converted_amount[0])
  var_eur.set(converted_amount[1])
  var_gbp.set(converted_amount[2])
  var_jpy.set(converted_amount[3])
  var_cny.set(converted_amount[4])


# Image label within image frame
image_label = tk.Label(image_frame)
image_label.pack()

# Run the main application loop
root.mainloop()
