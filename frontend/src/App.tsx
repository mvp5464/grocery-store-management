import { useEffect, useState } from "react";

interface products {
  name: string;
  price_per_unit: number;
  product_id: number;
  uom_id: number;
  uom_name: string;
}

function App() {
  const [data, setData] = useState<products[]>([]);

  // useEffect(() => {
  //   const body = JSON.stringify({ product_id: 8 });
  //   fetch("http://localhost:5000/deleteProduct", {
  //     method: "POST",
  //     headers: { "content-type": "application/json" },
  //     body: body,
  //   })
  //     .then((response) => response.json())
  //     .then((data) => console.log({ data }))
  //     .catch((error) => console.error("Error:", error));
  // }, []);

  useEffect(() => {
    const body = JSON.stringify({
      product_name: "potato",
      uom_id: "3",
      price_per_unit: "102",
    });
    fetch("http://localhost:5000/createProduct", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: body,
    })
      .then((res) => res.json())
      .then((data) => console.log({ data }))
      .catch((error) => console.error("Error:", error));
  }, []);

  useEffect(() => {
    fetch("http://localhost:5000/getProducts")
      .then((res) => res.json())
      .then((data) => {
        console.log({ data });
        setData(data.data);
      });
  }, []);
  return (
    <>
      <div className=" grid grid-cols-6 text-center">
        <div className=" bg-blue-50">No.</div>
        <div className=" bg-blue-50">product Id</div>
        <div className=" bg-blue-50">Product Name</div>
        <div className=" bg-blue-50">Price Per Unit</div>
        <div className=" bg-blue-50">Quantity</div>
        <div className=" bg-blue-50">Total Product Price</div>
      </div>
      {data.map((product, i) => (
        <div key={i} className=" grid grid-cols-6 text-center">
          <div className=" bg-blue-50">{i + 1}</div>
          <div className=" bg-blue-50">{product.product_id}</div>
          <div className=" bg-blue-50">{product.name}</div>
          <div className=" bg-blue-50">
            {product.price_per_unit} Rs/ {product.uom_name}
          </div>
        </div>
      ))}
    </>
  );
}

export default App;
