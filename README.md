# Bangalore Home Price Prediction

A web application that predicts home prices in Bangalore based on location, square footage, number of bedrooms (BHK), bathrooms, and balconies using machine learning.

## Features

- **Interactive Web Interface**: User-friendly form to input property details
- **Real-time Predictions**: Get instant price estimates using a trained ML model
- **Location-based Pricing**: Supports multiple Bangalore locations
- **Responsive Design**: Works on different screen sizes

## Tech Stack

- **Backend**: Python Flask API
- **Frontend**: HTML, CSS, JavaScript with jQuery
- **ML Model**: Scikit-learn Linear Regression
- **Data Processing**: NumPy, Pandas

## Project Structure

```
banglore_price_prediction/
├── Client/
│   ├── app.html          # Main web interface
│   ├── app.js            # Frontend JavaScript logic
│   └── app.css           # Styling
├── server/
│   ├── server.py         # Flask API server
│   ├── util.py           # ML model utilities
│   ├── artifacts/
│   │   ├── banglore_home_price_model  # Trained ML model
│   │   └── columns.json               # Model features
│   └── test_model.py    # Model testing script
└── model/
    ├── banglore_home_price_model      # Backup model file
    ├── columns.json                   # Backup features
    └── ds_project1.ipynb              # Jupyter notebook
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/banglore-price-prediction.git
cd banglore-price-prediction
```

### 2. Install Dependencies

```bash
cd server
pip install flask flask-cors numpy scikit-learn
```

### 3. Start the Flask Server

```bash
python server.py
```

You should see:
```
Starting Python Flask Server For Home Price Prediction...
loading saved artifacts..start
loading saved artifacts ...done
 * Running on http://127.0.0.1:5000
```

### 4. Open the Web Interface

Open `Client/app.html` in your web browser, or serve it through a local server.

**Important**: Due to CORS restrictions, you must open the HTML file in a web browser (not VS Code preview) for the application to work properly.

## Usage

1. **Enter Property Details**:
   - Square footage (e.g., 1000)
   - Number of bedrooms (BHK: 1-5)
   - Number of bathrooms (1-5)
   - Number of balconies (0-3)
   - Select location from dropdown

2. **Click "Estimate Price"**

3. **View Results**: The estimated price in lakhs will appear below the form

## API Endpoints

### GET /get_location_names
Returns available Bangalore locations for the dropdown.

**Response:**
```json
{
  "location": ["Electronic City", "Rajaji Nagar", ...]
}
```

### POST /predict_home_price
Predicts home price based on input parameters.

**Request Body (form-data):**
- `total_sqft`: float (square footage)
- `bhk`: int (number of bedrooms)
- `bath`: int (number of bathrooms)
- `balcony`: int (number of balconies)
- `location`: string (location name)

**Response:**
```json
{
  "estimated_price": 45.67
}
```

## Model Details

- **Algorithm**: Linear Regression
- **Features**: Square footage, BHK, bathrooms, balconies, location (one-hot encoded)
- **Target**: Price in lakhs (INR)
- **Training Data**: Bangalore real estate data

## Troubleshooting

### CORS Error
If you see CORS errors, ensure you're opening the HTML file in a real browser (Chrome/Firefox/Edge) and not VS Code's preview.

### Server Not Starting
- Check if port 5000 is available
- Ensure all dependencies are installed
- Verify model files exist in `server/artifacts/`

### No Price Prediction
- Check browser console for JavaScript errors
- Ensure Flask server is running
- Verify all form fields are filled

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built as part of a data science project
- Uses Bangalore real estate dataset
- Inspired by real-world property price prediction applications
