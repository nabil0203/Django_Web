function Product({ product }) {

    return (
        <div className="relative border-2 p-4 rounded-xl shadow-md w-64 hover:scale-101 cursor-pointer">

            <input type="checkbox" className="absolute top-6 right-6" />                                      {/* Checkbox for selecting the product*/}
            <img src={product.image}/>
            <p>{product.name}</p>
            <p>{product.price}</p>  

        </div>

    )


}


export default Product