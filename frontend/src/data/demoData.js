fetch("/result.json")
  .then((res) => res.json())
  .then((data) => {
    const formattedData = data.map((item) => ({
      bankName: item.bank_name,
      chequeNumber: item.cheque_number,
      date: item.date,
      amount: item.amount_number,
      amountword: item.amount_words,
      issuerName: item.payee_name,
      errorFlags: item.error_flags,
      warningFlags: item.warning_flags,
    }));

    setChequeRecords(formattedData);
  });