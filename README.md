
# Weather App 🌤️

A simple **Graphical user interface (GUI)** Weather App built with **Tkinter** that dislays current weather information of any city. It fetches weather information from [OpenWeatherMap API](https://openweathermap.org/) and displays it in an easy-to-understand format, including **temperature**, **wind speed**, and **weather conditions**.

## Technologies used

- **Python**: Main programming language.
- **Tkinter**: For GUI design.
- **Requests**: For API calls.
- **Pillow (PIL)**: For image processing.
- **OS**: For accessing environment variables securely (API Key)



## Prerequisites

- Python 3.7 or higher 
- Libraries:
   - `tkinter`
   - `requests`
   - `Pillow`

To install the required Python libraries. Open the terminal in the directory where ```requirements.txt``` is located and run the following command:

```bash
pip install -r requirements.txt
```
## Setting the API Key

This app fetches weather data from the OpenWeatherMap API, and you need an API key to use it. Here's how to set up your API key as a **Windows System Environment Variable**:

1. **Open the Environment Variables window**:
   - Right-click on **This PC** (or **My Computer**) and click on **Properties**.
   - Click on **Advanced system settings** on the left side.
   - In the **System Properties** window, click on the **Environment Variables** button near the bottom.

2. **Add a new system variable**:
   - In the **Environment Variables** window, under the "System variables" section, click on **New**.
   - In the **Variable name** field, enter:
     ```bash
     OPENWEATHERMAP_API_KEY
     ```
   - In the **Variable value** field, enter your **actual OpenWeatherMap API key**:
     ```bash
     your_api_key
     ```

3. **Save the changes**:
   - Click **OK** to add the variable, then click **OK** again to close the Environment Variables window.
   - Afterward, click **OK** in the System Properties window to finalize the changes.

4. **Restart the system (if necessary)**:
   - Some systems may require a restart for the changes to take effect, although usually, logging out and logging back in should work.

Once you’ve set the system environment variable, you don’t need to worry about manually entering it in your script or terminal each time you run the program. It will automatically be available for any applications or scripts you run.


## API Reference

### Get the weather data

```http
  GET https://api.openweathermap.org/data/2.5/weather
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `q` | `string` | **Required**. The name of the city for which weather is requested |
|`units`|`string`|Optional. The unit of measurement for temperature. Default is `metric`|

#### Example Request

```http
  GET https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}
```
#### Example Response

```json
{
  "main": {
    "temp": 22.5,
    "humidity": 78
  },
  "wind": {
    "speed": 5.1
  },
  "weather": [
    {
      "description": "clear sky",
      "icon": "01d"
    }
  ]
}
```

### Get Weather Icon

```http
   GET https://openweathermap.org/img/wn/{icon_id}.png
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `icon_id`| `string` | **Required**. The icon identifier (e.g., `01d` or `10n`) to fetch the weather icon |

#### Example Response

This will return the icon image file for the weather conditions (e.g., clear sky, rain, etc.).



