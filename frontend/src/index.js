import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Product from './Product'
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Product />
  </React.StrictMode>
);

reportWebVitals();
