import { useEffect, useState } from "react";

interface products {
  name: string;
  price_per_unit: number;
  product_id: number;
  uom_id: number;
  uom_name: string;
}

function Products() {
  const [data, setData] = useState<products[]>([]);
  const [isEdit, setIsEdit] = useState<number | null>(null);

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
  //   // }, []);

  //   useEffect(() => {
  //     const body = JSON.stringify({
  //       product_name: "potato",
  //       uom_id: "3",
  //       price_per_unit: "102",
  //     });
  //     fetch("http://localhost:5000/createProduct", {
  //       method: "POST",
  //       headers: { "content-type": "application/json" },
  //       body: body,
  //     })
  //       .then((res) => res.json())
  //       .then((data) => console.log({ data }))
  //       .catch((error) => console.error("Error:", error));
  //   }, []);

  function handleDeleteClick(product_id: number) {
    const body = JSON.stringify({
      product_id: product_id,
    });
    fetch("http://localhost:5000/deleteProduct", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: body,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log({ data });
        getProduct();
      })
      .catch((error) => console.error("Error:", error));
  }
  function getProduct() {
    fetch("http://localhost:5000/getProducts")
      .then((res) => res.json())
      .then((data) => {
        console.log({ data });
        setData(data.data);
      });
  }
  useEffect(() => {
    getProduct();
  }, []);
  return (
    <div className=" bg-slate-700 h-full p-10">
      <div className=" max-w-4xl mx-auto max-h-[80%] overscroll-y-auto bg-white">
        <div className=" grid grid-cols-5 text-center my-3 text-xl font-bold">
          <div className="">No.</div>
          <div className="">product Id</div>
          <div className="">Product Name</div>
          <div className="">Price Per Unit</div>
          <div className=" flex justify-around">
            <div className="">Actions</div>
            {/* <div className="">Delete</div> */}
          </div>
        </div>
        {data &&
          data.map((product, i) => (
            <div
              key={i}
              className=" grid grid-cols-5 text-center h-[90%] border hover:bg-blue-100"
            >
              <div className="">{i + 1}</div>
              <div className="">{product.product_id}</div>
              {isEdit == product.product_id ? (
                <>
                  <div>
                    <input type="text" value={product.name} />
                  </div>
                  <div>
                    <input type="text" value={product.price_per_unit} />
                  </div>
                </>
              ) : (
                <>
                  <div className="">{product.name}</div>
                  <div className="">
                    {product.price_per_unit} Rs/ {product.uom_name}
                  </div>
                </>
              )}
              <div className=" flex justify-around">
                <button
                  onClick={() => setIsEdit(product.product_id)}
                  className=" bg-blue-400 px-4 py-1 rounded-xl"
                >
                  {isEdit == product.product_id ? "Save" : "Edit"}
                </button>
                <button
                  className=" bg-red-400 px-4 py-1 rounded-xl"
                  onClick={() => handleDeleteClick(product.product_id)}
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default Products;
