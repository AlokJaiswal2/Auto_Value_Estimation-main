# Auto Value Estimation 🚗

Auto Value Estimation is a full-stack car price prediction application that estimates the market value of a car based on its specifications.

The project combines a **React + TypeScript frontend**, a **Python Flask backend**, and **machine learning models** for car price prediction.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Setup Instructions](#️-setup-instructions)
- [How to Run](#-how-to-run)
- [API Endpoints](#-api-endpoints)
- [Training the Model](#-training-the-model)
- [Technologies Used](#️-technologies-used)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Features

- **ML-Powered Predictions**: Uses machine learning models for car price estimation
- **Modern Frontend**: Built with React, TypeScript, Vite, and Tailwind CSS
- **RESTful API**: Flask backend with CORS support for frontend integration
- **Dynamic Form**: Car details can be entered through the frontend estimation form
- **Real-time Predictions**: Price predictions are requested through the backend API
- **Streamlit Demo**: Includes a Streamlit application for testing the prediction system

---

## 📁 Project Structure

```text
Auto_Value_Estimation-main/
│
├── Backend/
│   ├── api_server.py
│   ├── car_price_model_advanced.py
│   ├── clean_and_enhance_dataset.py
│   ├── fix_dataset_issues.py
│   ├── market_reference_prices.json
│   ├── model_advanced_metrics.json
│   ├── model_metrics_plot.png
│   ├── plot_model_metrics.py
│   └── requirements.txt
│
├── Frontend/
│   ├── public/
│   ├── src/
│   ├── bun.lockb
│   ├── components.json
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── Sports Car GIF by FaZe Clan.gif
│   ├── streamlit_app.py
│   ├── tailwind.config.ts
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
│
└── README.md
```

### Key Files Explained

**Backend:**

- `api_server.py` - Flask REST API server that serves car price predictions
- `car_price_model_advanced.py` - Script used to train/retrain the machine learning model
- `clean_and_enhance_dataset.py` - Script for cleaning and enhancing the dataset
- `fix_dataset_issues.py` - Script for fixing dataset-related issues
- `market_reference_prices.json` - Market reference price data used by the prediction system
- `model_advanced_metrics.json` - Stores model performance metrics
- `model_metrics_plot.png` - Visualization of model performance metrics
- `plot_model_metrics.py` - Script for generating model metric plots
- `requirements.txt` - Python dependencies required for the backend

**Frontend:**

- `src/` - Main React/TypeScript source code
- `public/` - Public static assets
- `package.json` - Frontend dependencies and npm scripts
- `vite.config.ts` - Vite configuration
- `tailwind.config.ts` - Tailwind CSS configuration
- `components.json` - UI component configuration
- `streamlit_app.py` - Streamlit-based prediction interface
- `Sports Car GIF by FaZe Clan.gif` - Frontend visual asset

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed
- **Node.js 18+** and **npm** installed
- Ensure you're in the `Auto_Value_Estimation-main` directory

### Step-by-Step Setup

1. **Install backend dependencies:**

   ```bash
   cd Backend
   pip install -r requirements.txt
   ```

2. **Install frontend dependencies:**

   ```bash
   cd ../Frontend
   npm install
   ```

3. **Start backend server (Terminal 1):**

   ```bash
   cd Backend
   python api_server.py
   ```

   The backend API will start on the configured Flask port.

4. **Start frontend (Terminal 2):**

   ```bash
   cd Frontend
   npm run dev
   ```

5. **Open the frontend:**

   Vite will display the local development URL in the terminal, typically:

   ```text
   http://localhost:5173/
   ```

---

## 🛠️ Setup Instructions

### Backend Setup

1. **Navigate to the backend directory:**

   ```bash
   cd Auto_Value_Estimation-main/Backend
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask API server:**

   ```bash
   python api_server.py
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd Auto_Value_Estimation-main/Frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the Vite development server:**

   ```bash
   npm run dev
   ```

   The terminal will show the local frontend URL.

---

## 🔌 API Endpoints

The Flask backend provides REST API endpoints for communicating with the frontend.

### `GET /api/health`

Health check endpoint.

**Example Response:**

```json
{
  "status": "healthy",
  "model_loaded": true,
  "dataset_loaded": true
}
```

### `GET /api/metrics`

Returns machine learning model performance metrics.

**Example Response:**

```json
{
  "MAE": 22211.80,
  "RMSE": 29602.85,
  "R2": 0.9983
}
```

### `GET /api/options`

Returns available options used by the frontend estimation form.

**Example Response:**

```json
{
  "brands": ["Honda", "Toyota"],
  "models": ["City", "Civic"],
  "fuel_types": ["Petrol", "Diesel", "CNG", "Electric"],
  "transmissions": ["Manual", "Automatic"]
}
```

### `GET /api/models?brand=<brand_name>`

Returns available car models for a selected brand.

**Example Response:**

```json
{
  "models": ["City", "Civic", "Amaze"]
}
```

### `POST /api/predict`

Predicts the estimated price of a car.

**Example Request Body:**

```json
{
  "Brand": "Honda",
  "Model": "City",
  "Year": 2020,
  "Fuel_Type_Clean": "Petrol",
  "Transmission_Clean": "Manual",
  "Mileage_Clean": 18.5,
  "Engine_CC_Clean": 1500,
  "Seating_Capacity_Clean": 5,
  "Service_Cost_Clean": 10000
}
```

**Example Response:**

```json
{
  "predicted_price": 1608000.0,
  "predicted_price_formatted": "₹ 1,608,000",
  "input_data": {}
}
```

---

## 🔄 Frontend-Backend Connection

The frontend and backend communicate through the Flask REST API.

1. **API Configuration**: The frontend sends requests to the Flask backend.
2. **Form Component**: The React frontend collects car specifications and submits prediction requests.
3. **Dynamic Data**: The frontend can retrieve available car options and models through API endpoints.
4. **Prediction Request**: The completed car details are sent to `/api/predict`.
5. **CORS**: Flask-CORS allows the frontend to communicate with the backend during development.

---

## 🎯 How to Run the Project

### Method 1: Quick Start (Recommended)

**Terminal 1 - Backend:**

```bash
cd Auto_Value_Estimation-main/Backend

pip install -r requirements.txt

python api_server.py
```

**Terminal 2 - Frontend:**

```bash
cd Auto_Value_Estimation-main/Frontend

npm install

npm run dev
```

**Then:**

- Open the frontend URL displayed by Vite.
- The frontend communicates with the Flask API running in the backend.

### Method 2: Step-by-Step

1. **Open Terminal 1 - Start Backend:**

   ```bash
   cd Auto_Value_Estimation-main/Backend
   python api_server.py
   ```

2. **Open Terminal 2 - Start Frontend:**

   ```bash
   cd Auto_Value_Estimation-main/Frontend
   npm run dev
   ```

3. **Open Browser:**

   Open the local URL shown in the Vite terminal output.

### Using the Application

1. **Fill out the car estimation form:**
   - **Brand**: Select the car brand
   - **Model**: Select the car model
   - **Year**: Select the manufacturing year
   - **Fuel Type**: Select the fuel type
   - **Transmission**: Select the transmission type
   - **Mileage**: Enter the vehicle mileage
   - **Engine CC**: Enter the engine capacity
   - **Seating Capacity**: Enter/select the seating capacity
   - **Service Cost**: Enter the service cost

2. **Click the price estimation button.**
3. **View the estimated car value** returned by the machine learning model.

---

## 🧪 Training the Model

The machine learning training scripts are located inside the `Backend/` directory.

To train or retrain the model, first navigate to the backend directory:

```bash
cd Auto_Value_Estimation-main/Backend
```

Then run the training script according to its supported arguments:

```bash
python car_price_model_advanced.py
```

Dataset cleaning and enhancement scripts are also available:

```bash
python clean_and_enhance_dataset.py
```

```bash
python fix_dataset_issues.py
```

Model metrics can be visualized using:

```bash
python plot_model_metrics.py
```

---

## 📊 Model Performance

Model performance metrics are stored in:

```text
Backend/model_advanced_metrics.json
```

The project also includes:

```text
Backend/model_metrics_plot.png
```

which can be used to visualize the model's performance metrics.

---

## 🛠️ Technologies Used

### Backend

- Python
- Flask
- Flask-CORS
- scikit-learn
- XGBoost / LightGBM
- pandas
- NumPy
- joblib
- JSON

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- JavaScript / JSX
- HTML5
- CSS3

### Machine Learning

- Data preprocessing
- Feature engineering
- Regression models
- Model evaluation
- MAE
- RMSE
- R² Score

---

## 🐛 Troubleshooting

### Backend Issues

1. **Dependencies not installed:**

   ```bash
   cd Backend
   pip install -r requirements.txt
   ```

2. **API server does not start:**
   - Check that Python is installed.
   - Verify all required dependencies are installed.
   - Make sure you are running the command from the `Backend/` directory.

3. **Model or dataset file not found:**
   - Verify that all required model and dataset files used by `api_server.py` are present in the backend directory.
   - Check the file paths configured in the backend scripts.

4. **Port already in use:**
   - Stop the process using the Flask port or change the port configuration in `api_server.py`.

### Frontend Issues

1. **Cannot connect to API:**
   - Ensure the backend server is running.
   - Check the API URL used by the frontend.
   - Check the browser console for CORS errors.

2. **Dependencies are missing:**

   ```bash
   cd Frontend
   npm install
   ```

3. **Frontend does not start:**
   - Verify that Node.js and npm are installed.
   - Check the terminal for Vite configuration or dependency errors.

4. **Form options are not loading:**
   - Make sure the backend API is running.
   - Verify that the required API endpoint is available.
   - Check the browser Network tab for failed requests.

---

## 📝 Notes

- The backend contains the machine learning training, preprocessing, and API scripts.
- The frontend contains the React/TypeScript application.
- `streamlit_app.py` provides a Streamlit interface for the prediction system.
- Model performance information is stored in `model_advanced_metrics.json`.
- Market reference data is stored in `market_reference_prices.json`.
- Run backend commands from the `Backend/` directory.
- Run frontend commands from the `Frontend/` directory.

---

## 📄 License

This project is for educational/demonstration purposes.

---

## 🤝 Contributing

Feel free to submit issues and enhancement requests!
