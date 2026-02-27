import * as XLSX from "xlsx";
import { saveAs } from "file-saver";

export const exportChequeDataToExcel = (records) => {
  if (!records || records.length === 0) {
    alert("No data available to download");
    return;
  }

  // Remove accuracy & issue columns
  const exportData = records.map(
    ({
      bankName,
      chequeNumber,
      date,
      amount,
      amountword,
      issuerName,
    }) => ({
      "Bank Name": bankName,
      "Cheque Number": chequeNumber,
      "Date": date,
      "Amount": amount,
      "Amount in Words": amountword,
      "Issuer Name": issuerName,
    })
  );

  const worksheet = XLSX.utils.json_to_sheet(exportData);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Cheque Data");

  const excelFile = XLSX.write(workbook, {
    bookType: "xlsx",
    type: "array",
  });

  const blob = new Blob([excelFile], {
    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  });

  saveAs(blob, "Cheque_Data.xlsx");
};