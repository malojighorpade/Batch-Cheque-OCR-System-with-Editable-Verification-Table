import { demoChequeRecords } from "../data/demoData";

const calculateAccuracy = (row) => {
  const requiredFields = [
    row.bankName,
    row.chequeNumber,
    row.date,
    row.amount,
    row.amountword,
    row.issuerName,
  ];

  const filled = requiredFields.filter(
    (field) => field && field.toString().trim() !== ""
  ).length;

  return Math.round((filled / requiredFields.length) * 100);
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

export const processFile = (file, onProgress) => {
  return new Promise((resolve) => {
    let progress = 0;

    const interval = setInterval(() => {
      progress += 20;
      onProgress(progress);

      if (progress >= 100) {
        clearInterval(interval);

        const processedData = demoChequeRecords.map((row) => {
          const accuracy = calculateAccuracy(row);
          const issue = detectIssue(row, accuracy);

          return {
            ...row,
            accuracy,
            issue,
          };
        });

        resolve(processedData);
      }
    }, 400);
  });
};