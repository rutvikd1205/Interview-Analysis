// static/script.js
document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/process', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById('conversation').innerText = response.conversation;
            document.getElementById('output').innerText = response.result;
        } else {
            console.error('Request failed. Error code: ' + xhr.status);
        }
    };
    xhr.onerror = function() {
        console.error('Request failed');
    };
    xhr.send(formData);
});

document.querySelectorAll('input[name="input_type"]').forEach(function(inputType) {
    inputType.addEventListener('change', function() {
        if (this.value === 'text') {
            document.getElementById('text_input_group').style.display = 'block';
            document.getElementById('audio_file_group').style.display = 'none';
            // Clear audio input field
            document.getElementById('audio_file').value = '';
        } else if (this.value === 'audio') {
            document.getElementById('text_input_group').style.display = 'none';
            document.getElementById('audio_file_group').style.display = 'block';
            // Clear text input field
            document.getElementById('text_file').value = '';
        }
    });
});
