import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Product() {
    const product1 = React.createRef();
    const product2 = React.createRef();
    const product3 = React.createRef();
    const product4 = React.createRef();
    const update_product1 = React.createRef();
    const update_product2 = React.createRef();
    const update_product3 = React.createRef();

    const [product, setProduct] = useState([]);
    const [message, setMessage] = useState('');

    useEffect(() => {
        console.log("request to api");
        axios.get("http://127.0.0.1:5000/products")
            .then(response => setProduct(response.data))
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [product]);

    let productList;
    if (Array.isArray(product)) {
        productList = product.map(p => (
            <li key = {p._id}>
                ID : {p._id}
                <span> {p.name}</span>
                <img src={p.img}/> 
                {p.price}
                <button onClick={() => onDeleteProducts(p._id)}>Delete</button>
                <button onClick={() => onOkClick(p._id)}>ok</button>
            </li>
        ));
    } else {
        productList = []; 
    }

    const onAddProduct = () => {
        const data = {
            _id: parseInt(product1.current.value),
            name: product2.current.value,
            price: product3.current.value,
            img: product4.current.value
        };
        axios.post("http://127.0.0.1:5000/products", data)
            .then((response) => {
                setProduct(response.data)
                setMessage('Add Product Successfuly')
            })
            .catch(error => {
                console.error('Error', error);
                setMessage(error.response.data.message || 'An error occurred while adding the product.');
            });
    };

    const onDeleteProducts = (id) => {
        console.log("DELETE " + id);
        axios.delete(`http://127.0.0.1:5000/products/${id}`)
            .then((response) => setProduct(response.data))
            .catch(error => {
                console.error('Error', error);
                setMessage(error.response.data.message || 'An error occurred while deleting the product.');
            });        
    };
    
    const onOkClick = (id) => {
        console.log("UPDATE " + id);
        const data = {
            name: update_product1.current.value,
            price: update_product2.current.value,
            img: update_product3.current.value
        };
        axios.put(`http://127.0.0.1:5000/products/${id}`, data)
            .then((response) => {
                setProduct(response.data)
                setMessage('Update Successfuly!')
            })
            .catch(error => {
                console.error('Error', error);
                setMessage(error.response.data.message || 'An error occurred while updating the product.');
            });
    };

    if (!product) return null;

    return (
        <div style = {{ textAlign: "center" }}>
            <div style = {{ margin: "20px auto", maxWidth: "600px" }}>
                <h1>Add Product</h1>
                <div>{message && <p>{message}</p>}</div>
                    <div>
                        <label htmlFor = "product_id">ID:</label>
                        <input type = "number" id = "product_id" ref = {product1} />
                    </div>
                    <div>
                        <label htmlFor = "product_name">Product Name:</label>
                        <input type = "text" id = "product_name" ref = {product2} />
                    </div>
                    <div>
                        <label htmlFor = "product_price">Price:</label>
                        <input type = "text" id="product_price" ref = {product3} />
                    </div>
                    <div>
                        <label htmlFor = "product_img">Image URL:</label>
                        <input type = "text" id = "product_img" ref = {product4} />
                    </div>
                <button onClick={onAddProduct}>Add Product</button>
            </div>

            <div style = {{ margin: "20px auto", maxWidth: "600px" }}>
                <h1>Update Product</h1>
                <h2>Select a product to update</h2>
                <div>
                    <label htmlFor="update_product_name">Product Name:</label>
                    <input type = "text" id="update_product_name" ref = {update_product1} />
                </div>
                <div>
                    <label htmlFor="update_product_price">Price:</label>
                    <input type = "text" id="update_product_price" ref = {update_product2} />
                </div>
                <div>
                    <label htmlFor = "update_product_img">Image URL:</label>
                    <input type = "text" id = "update_product_img" ref = {update_product3} />
                </div>
            </div>

            <div style={{ margin: "20px auto", maxWidth: "800px" }}>
                <h1>Products</h1>
                <ul style={{ listStyleType: "none", padding: 0 }}>{productList}</ul>
            </div>
        </div>
    );
}
