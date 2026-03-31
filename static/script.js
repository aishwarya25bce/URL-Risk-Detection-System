function startQR() {
    const qr = new Html5Qrcode("reader");

    qr.start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        (decodedText) => {
            document.getElementById("urlInput").value = decodedText;
            qr.stop();
        }
    );
}