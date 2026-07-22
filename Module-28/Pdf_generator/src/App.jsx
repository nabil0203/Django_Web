import './App.css'
import Invoice from './Invoice'
import { useState } from 'react'
import { PDFViewer, PDFDownloadLink } from '@react-pdf/renderer'
import Product from './Product'



// Array of objects for product list
const products = [
  { id: 1, name: 'Product A', price: '$10', image: 'https://picsum.photos/300/400'},
  { id: 2, name: 'Product B', price: '$20', image: 'https://picsum.photos/300/400'},
  { id: 3, name: 'Product C', price: '$30', image: 'https://picsum.photos/300/400'},
  { id: 4, name: 'Product D', price: '$40', image: 'https://picsum.photos/300/400'},
  { id: 5, name: 'Product E', price: '$50', image: 'https://picsum.photos/300/400'},
]



function App() {
 
  const [showPDF, setShowPDF] = useState(false)

  const [selectedProducts, setSelectedProducts] = useState([])                 // State to keep track of selected products; initially an empty array-> no products are selected

  function openPdf() {
    
    // setShowPDF(true)                 // only shows the PDF but doesn't hide on click
    setShowPDF(!showPDF)                // Shows and hides the PDF on click

  }



  return (
    <>
      
      {/* ---------Show product List------------ */}
      
      <div className="p-24">
        <h1 className="text-2xl font-bold mb-4">All Products</h1>

        <div className="flex gap-4">
          {
            products.map(product => {
              return < Product key={product.id} product={product} />               // Loop through the products array and render a Product component for each product, passing the product details as arguments
            })
          }
        </div>
        
      </div>
      



      {/*----------Show pdf button--------- */}
      <button onClick={openPdf} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        {showPDF ? 'Hide PDF' : 'Show PDF'}
      </button>




      {/*---------Download PDF Button-----------*/}
      <PDFDownloadLink 
        document={<Invoice />} 
        fileName="invoice.pdf" 
        className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded ml-4"
      >
        {
          ({ blob, url, loading, error }) =>
            loading ? 'Generating PDF ... ' : 'Download PDF'                              // Show loading text while PDF is being generated, otherwise always show Download Button
        }

      </PDFDownloadLink>


      

      {/* {showPDF ? <Invoice /> : null} */}                                              {/* ---- if showPDF is true, display the Invoice component -------*/}              
      {showPDF ? 

      <PDFViewer style={{ width: '700px', height: '700px', margin: '20px' }}>

        <Invoice />

      </PDFViewer>
      
      : null}




    </>
  )
}

export default App
