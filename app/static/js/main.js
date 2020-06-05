(function () {
	window.video_service = {};

	$('.tool form').on('submit', function (e) {
		e.preventDefault();
		var files = $(e.target).find('.tool__file').get(0).files;
		var file = files[0];
		if (!file) {
			return alert('No file selected.');
		}
		getSignedRequest(file, e.target);
	});

	function getSignedRequest(file, target) {
		$.get({
			url: '/video/sign_s3',
			dataType: 'json',
			data: {
				file_name: file.name,
				file_type: file.type
			}
		}).done(function (response) {
			uploadFile(file, response);
			sendData(file, $(target).serializeArray());
		}).fail(function (err) {
			console.log(err);
			alert('Could not get signed URL.');
		});
	}

	function uploadFile(file, s3Data) {
		if (window.location.protocol === 'http:') return alert('uploading is only allowed from https');
		var postData = new FormData();
		for (key in s3Data.data.fields) {
			postData.append(key, s3Data.data.fields[key]);
		}
		postData.append('file', file);

		$.ajax({
			type: 'POST',
			url: s3Data.url,
			enctype: 'multipart/form-data',
			processData: false,
			contentType: false,
			cache: false,
			data: postData
		}).done(function (response) {
			console.log('success', response);
		}).fail(function (err) {
			console.log(err);
			alert('Could not upload file.' + err);
		});
	}

	function sendData(file, data) {
		data.push({name: 'file_name', value: file.name});
		$.post('/video/save', data).done(function (response) {
		}).fail(function (err) {
			console.log(err);
		});
	}
})();
