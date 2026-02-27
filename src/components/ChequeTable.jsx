import { useState } from "react";
import { toast } from "react-toastify";

function ChequeTable({ records = [], setRecords }) {
  const [editIndex, setEditIndex] = useState(null);
  const [editData, setEditData] = useState({});

  const calculateAccuracy = (row) => {
    const required = [
      row.bankName,
      row.chequeNumber,
      row.date,
      row.amount,
      row.amountword,
      row.issuerName,
    ];

    const filled = required.filter(
      (field) => field && field.toString().trim() !== ""
    ).length;

    return Math.round((filled / required.length) * 100);
  };

  const detectIssue = (row, accuracy) => {
    if (!row.amount || Number(row.amount) <= 0)
      return "Invalid Amount";
    if (!row.chequeNumber)
      return "Missing Cheque Number";
    if (!row.amountword)
      return "Missing Amount in Words";
    if (!row.date)
      return "Missing Date";
    if (!row.bankName)
      return "Missing Bank Name";
    if (!row.issuerName)
      return "Missing Issuer Name";
    if (accuracy < 80)
      return "Low Accuracy";

    return "OK";
  };

  const handleEditClick = (index) => {
    setEditIndex(index);
    setEditData({ ...records[index] });
  };

  const handleChange = (e, field) => {
    setEditData({
      ...editData,
      [field]: e.target.value,
    });
  };

  const handleSave = () => {
    const accuracy = calculateAccuracy(editData);
    const issue = detectIssue(editData, accuracy);

    const updatedRow = {
      ...editData,
      accuracy,
      issue,
    };

    const updatedRecords = [...records];
    updatedRecords[editIndex] = updatedRow;

    setRecords(updatedRecords);
    setEditIndex(null);

    toast.success("Row updated successfully ✅");
  };

  return (
    <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "30px" }}>
      <thead>
        <tr>
          <th>Cheque ID</th>
          <th>Bank Name</th>
          <th>Cheque Number</th>
          <th>Date</th>
          <th>Amount</th>
          <th>Amount in Words</th>
          <th>Issuer Name</th>
          <th>Accuracy (%)</th>
          <th>Issue</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>
        {records.map((row, index) => {
          const isEditing = editIndex === index;

          return (
            <tr key={index}>
              <td>{index + 1}</td>

              <td>
                {isEditing ? (
                  <input
                    value={editData.bankName || ""}
                    onChange={(e) => handleChange(e, "bankName")}
                  />
                ) : (
                  row.bankName || "-"
                )}
              </td>

              <td>
                {isEditing ? (
                  <input
                    value={editData.chequeNumber || ""}
                    onChange={(e) => handleChange(e, "chequeNumber")}
                  />
                ) : (
                  row.chequeNumber || "-"
                )}
              </td>

              <td>
                {isEditing ? (
                  <input
                    type="date"
                    value={editData.date || ""}
                    onChange={(e) => handleChange(e, "date")}
                  />
                ) : (
                  row.date || "-"
                )}
              </td>

              <td>
                {isEditing ? (
                  <input
                    type="number"
                    value={editData.amount || ""}
                    onChange={(e) => handleChange(e, "amount")}
                  />
                ) : (
                  row.amount || "-"
                )}
              </td>

              <td>
                {isEditing ? (
                  <input
                    value={editData.amountword || ""}
                    onChange={(e) => handleChange(e, "amountword")}
                  />
                ) : (
                  row.amountword || "-"
                )}
              </td>

              <td>
                {isEditing ? (
                  <input
                    value={editData.issuerName || ""}
                    onChange={(e) => handleChange(e, "issuerName")}
                  />
                ) : (
                  row.issuerName || "-"
                )}
              </td>

              <td>{row.accuracy}%</td>
              <td>{row.issue}</td>

              <td>
                {isEditing ? (
                  <>
                    <button onClick={handleSave}>Save</button>
                    <button onClick={() => setEditIndex(null)}>Cancel</button>
                  </>
                ) : (
                  <button onClick={() => handleEditClick(index)}>
                    Edit
                  </button>
                )}
              </td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default ChequeTable;