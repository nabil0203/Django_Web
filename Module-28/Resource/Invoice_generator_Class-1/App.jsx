
import { useState } from 'react'
import './App.css'
import Invoice from './Invoice'
import { PDFViewer, PDFDownloadLink } from '@react-pdf/renderer';
import Toon from './Toon';

function App() {

  const [showPDF, setShowPDF] = useState(false)

  function handleClick() {
    setShowPDF(!showPDF)
  }

  return (
    <>
      <button className='bg-black p-4 text-white mr-6 cursor-pointer' onClick={handleClick}>{showPDF ? "Hide Pdf" : "Show Pdf"}</button>
      <PDFDownloadLink 
          document={<Invoice />} 
          fileName="invoice.pdf"
          className='bg-black p-4 text-white'
        >
          {({ blob, url, loading, error }) =>
            loading ? 'Generating PDF...' : 'Download PDF'
          }
        </PDFDownloadLink>
      {showPDF ? 
      <div className='h-[80vh] w-[700px] mt-6'>
      <PDFViewer showToolbar={true} style={{width: '100%', height: '100%'}}>
      <Invoice />
      </PDFViewer>
      </div>
      : null}
      <Toon/>
    </>
  )
}

export default App
