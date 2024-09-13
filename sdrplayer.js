    // Fonction pour changer l'URL de l'iframe en fonction de la sélection
    function changeIframeURL() {
        var selector = document.getElementById("siteSelector");
        var iframe = document.getElementById("myIframe");
        var selectedURL = selector.value;

        // Changer la source de l'iframe à l'URL sélectionnée
        iframe.src = selectedURL;
    }

    // Fonction pour couper/démuter le son de la page
    function toggleMute() {
        var iframe = document.getElementById("myIframe");
        iframe.muted = !iframe.muted; // alterne entre mute et unmute
    }

    // Fonction pour zoomer/dézoomer la page
    function zoomIn() {
        var iframe = document.getElementById("myIframe");
        var currentZoom = iframe.style.zoom ? parseFloat(iframe.style.zoom) : 1;
        iframe.style.zoom = currentZoom + 0.1; // augmente le zoom de 10%
    }

    function zoomOut() {
        var iframe = document.getElementById("myIframe");
        var currentZoom = iframe.style.zoom ? parseFloat(iframe.style.zoom) : 1;
        iframe.style.zoom = currentZoom - 0.1; // réduit le zoom de 10%
    }

    // Fonction pour actualiser l'iframe
    function refreshIframe() {
        var iframe = document.getElementById("myIframe");
        iframe.src = iframe.src; // recharge la même source
    }

    // Fonction pour aller à la page précédente
    function goBack() {
        window.history.back(); // utilise l'historique du navigateur pour revenir
    }

    // Fonction pour aller à la page suivante
    function goForward() {
        window.history.forward(); // utilise l'historique du navigateur pour avancer
    }
