import './App.css'
import Invoice from './Invoice'
import { useState } from 'react'
import { PDFViewer, PDFDownloadLink } from '@react-pdf/renderer'

function App() {
 
  const [showPDF, setShowPDF] = useState(false)

  function openPdf() {
    
    // setShowPDF(true)                 // only shows the PDF but doesn't hide on click
    setShowPDF(!showPDF)                // Shows and hides the PDF on click

  }


  return (
    <>
      

      {/*----------Show pdf--------- */}
      <button onClick={openPdf} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        {showPDF ? 'Hide PDF' : 'Show PDF'}
      </button>



      {/*---------Download PDF-----------*/}
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


      
      {/* {showPDF ? <Invoice /> : null} */}
      {showPDF ? 

      <PDFViewer style={{ width: '700px', height: '600px', margin: '20px' }}>

        <Invoice />

      </PDFViewer>
      
      : null}




    </>
  )
}

export default App
