window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const element = this.document.getElementById("invoiceo");
            console.log(element);
            // console.log(window);
            var opt = {
                margin: 1,
                filename: 'myfile.pdf',
                image: { type: 'jpeg', quality: 1.98 },
                html2canvas: { scale: 3 },
                jsPDF: { unit: 'in', format: 'A4', orientation: 'portrait' }
            };

            html2pdf().set(opt).from(element).save();
        });
}