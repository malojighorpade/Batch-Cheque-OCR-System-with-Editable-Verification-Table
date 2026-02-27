import { useState } from "react";
import { processFile } from "./services/processingService";
import ChequeTable from "./components/ChequeTable";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { exportChequeDataToExcel } from "./utils/exportExcel";

function App() {
  const [file, setFile] = useState(null);
  const [fileURL, setFileURL] = useState(null);
  const [progress, setProgress] = useState(0);
  const [processing, setProcessing] = useState(false);
  const [records, setRecords] = useState([]);

  // ==============================
  // File Upload
  // ==============================
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    if (selectedFile.size > 4 * 1024 * 1024) {
      alert("File must be under 4MB");
      return;
    }

    setFile(selectedFile);

    // Create preview URL
    const url = URL.createObjectURL(selectedFile);
    setFileURL(url);
  };

  // ==============================
  // Process File
  // ==============================
  const handleProcess = async () => {
    if (!file) {
      alert("Upload file first");
      return;
    }

    setProcessing(true);
    setProgress(0);

    const result = await processFile(file, setProgress);
    setRecords(result);

    setProcessing(false);
  };

  // ==============================
  // View File
  // ==============================
  const handleViewFile = () => {
    if (fileURL) {
      window.open(fileURL, "_blank");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>🏦 Cheque Data Extraction System</h1>

      {/* Upload Section */}
      <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <input
          type="file"
          accept=".pdf,image/*"
          onChange={handleFileChange}
        />

        {/* Show View Button Only After Upload */}
        {file && (
          <button onClick={handleViewFile}>
            View
          </button>
        )}
      </div>

      <button onClick={handleProcess} style={{ marginTop: "10px" }}>
        Process
      </button>

      {/* Progress Bar */}
      {processing && (
        <div style={{ marginTop: "20px" }}>
          <div style={{ width: "100%", backgroundColor: "#ddd" }}>
            <div
              style={{
                width: `${progress}%`,
                backgroundColor: "#4caf50",
                color: "white",
                textAlign: "center",
              }}
            >
              {progress}%
            </div>
          </div>
        </div>
      )}

      {/* Table */}
      <ChequeTable records={records} setRecords={setRecords} />

      {/* Download Button */}
      {records.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <button onClick={() => exportChequeDataToExcel(records)}>
            Download Excel
          </button>
        </div>
      )}

      <ToastContainer position="top-right" autoClose={2000} />
    </div>
  );
}

export default App;