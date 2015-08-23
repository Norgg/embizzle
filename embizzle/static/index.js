function countdown(seconds) {
    if (seconds > 0) {
        $('#countdown').text(Math.floor(seconds));
        setTimeout(countdown, 1000, seconds-1);
    } else {
        location.reload();
    }
}
