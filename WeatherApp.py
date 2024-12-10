import requests
from tkinter import *
from tkinter import messagebox
from io import BytesIO
from PIL import Image,ImageTk
import os


def get_weather():
    API_key = os.getenv('OPENWEATHERMAP_API_KEY')
    print(API_key)
    cityname = city.get()

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&APPID={API_key}")
    

    if response.status_code == 200:
        data = response.json()
        
        temp = data['main']['temp']
        wins = data['wind']['speed']
        icon_id = data['weather'][0]['icon']
        desc=data['weather'][0]['description']

        icon=requests.get(f"http://openweathermap.org/img/wn/{icon_id}.png")
        icon=icon.content
        icon=Image.open(BytesIO(icon))
        icon=icon.resize((100,100),Image.LANCZOS)
        icon=ImageTk.PhotoImage(icon)

        icon_label.config(image=icon)
        icon_label.image=icon

        weather_info = f'Temperature: {temp}°C\nWind Speed: {wins} km/h\n\n{desc}'
        weather_label.config(text=weather_info)
    else:
        errormsg=response.text
        messagebox.showerror("Error","City Not Found")

root = Tk()
root.title("Weather App")
root.geometry("450x450")
root.resizable(False,False)


bg_label=Label(root,bg='#87CEEB')
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

txt_label=Label(root,text="Enter City Name",font=("helvatica",15),bg='#87CEEB')
txt_label.pack(pady=10)
city = Entry(root, font=("Arial", 14),justify="center")
city.pack(pady=10)
search = Button(root, text="Get Weather", command=get_weather)
search.pack(pady=20)

icon_label=Label(root,image="",bg='#87CEEB')
icon_label.pack(pady=5)


weather_label = Label(root, font=("Arial", 14),bg="#87CEEB")
weather_label.pack(pady=20)

root.mainloop()