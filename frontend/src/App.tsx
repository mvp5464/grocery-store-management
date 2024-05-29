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

  useEffect(() => {
    fetch("http://localhost:5000/getProducts")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log({ data });
      });
  }, []);
  return (
    <>
      {data.map((product) => (
        <div className=" flex border justify-around">
          <div className=" bg-blue-50">{product.name}</div>
          <div className=" bg-blue-50">{product.price_per_unit}</div>
          <div className=" bg-blue-50">{product.product_id}</div>
          <div className=" bg-blue-50">{product.uom_id}</div>
          <div className=" bg-blue-50">{product.uom_name}</div>
        </div>
      ))}
    </>
  );
}

export default App;
