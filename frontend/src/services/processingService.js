export const processFile = async (file, onProgress) => {
  try {
    onProgress(30);

    const response = await fetch("/result.json");

    onProgress(70);

    const backendData = await response.json();

    onProgress(100);

    const formattedData = backendData.map((item) => {
      const hasError = item.error_flags && item.error_flags.length > 0;

      return {
        bankName: item.bank_name,
        chequeNumber: item.cheque_number,
        date: item.date,
        amount: item.amount_number,
        amountword: item.amount_words,
        issuerName: item.payee_name,
        errorFlags: item.error_flags,
        warningFlags: item.warning_flags,
        accuracy: hasError ? 70 : 100,
        issue: hasError ? "Has Errors" : "OK",
      };
    });

    return formattedData;
  } catch (error) {
    console.error("Processing error:", error);
    return [];
  }
};