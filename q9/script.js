// script.js
function calculateTotal() {
  let grandTotal = 0;
  const rows = document.querySelectorAll("#billTable tr");

  rows.forEach((row, index) => {
    if (index > 0) {
      // Skip the header row
      const quantityInput = row.querySelector('input[id^="quantity"]');
      const priceInput = row.querySelector('input[id^="price"]');
      const totalSpan = row.querySelector(".total");

      if (!quantityInput || !priceInput || !totalSpan) {
        console.error("One or more required elements not found.");
        return; // Exit early if any required element is missing
      }

      const quantity = parseFloat(quantityInput.value) || 0;
      const price = parseFloat(priceInput.value) || 0;
      const total = quantity * price;

      totalSpan.textContent = total.toFixed(2);
      grandTotal += total;
    }
  });

  document.getElementById("grandTotal").textContent = grandTotal.toFixed(2);
}

function printBill() {
    let printSection = document.getElementById("printSection");
    printSection.innerHTML = "";

    let content = `
        <h1>Bill</h1>
        <table border="1">
            <tr>
                <th>Item</th>
                <th>Quantity</th>
                <th>Price per Unit</th>
                <th>Total</th>
            </tr>`;

    const rows = document.querySelectorAll("#billTable tr");
    rows.forEach((row, index) => {
        if (index > 0) { // Skip the header row
            const itemInput = row.querySelector('input[id^="item"]');
            const quantityInput = row.querySelector('input[id^="quantity"]');
            const priceInput = row.querySelector('input[id^="price"]');
            const totalSpan = row.querySelector(".total");

            if (itemInput && quantityInput && priceInput && totalSpan) {
                const item = itemInput.value;
                const quantity = quantityInput.value;
                const price = priceInput.value;
                const total = totalSpan.textContent;

                content += `
                    <tr>
                        <td>${item}</td>
                        <td>${quantity}</td>
                        <td>${price}</td>
                        <td>${total}</td>
                    </tr>`;
            } else {
                console.error("One or more required elements not found.");
            }
        }
    });

    content += `
        </table>
        <h2>Grand Total: ${document.getElementById("grandTotal").textContent}</h2>`;

    printSection.innerHTML = content;
    printSection.style.display = "block";  
    window.print();
    printSection.style.display = "none";  
}

