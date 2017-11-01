var getProblem = function(operation){
	$.get('/api/generate/2/' + operation, function(d){
		$('#problem').html(
			d.text
			+ '<div class="row">'
			  + '<div class="col-lg-4">'
			    + '<div class="input-group">'
			      + '<span class="input-group-btn">'
			        + '<button id="submit_answer" class="btn btn-primary" type="button">Submit!</button>'
			      + '</span>'
			      + '<input id="answer" type="text" class="form-control" placeholder="Put Answer Here...">'
			    + '</div>'
			  + '</div>'
			+ '</div>'
		);
		$('#submit_answer').on('click', function(event){
			var answer = $('#answer').val().trim();
			var terms = d.problem.terms;
			$.get('/api/check/' + operation + '/' + terms[0] + '/' + terms[1] + '/' + answer, function(data){
				if (data.correct){
					$.notify({
						title: 'Correct!!',
						message: 'Way to go!'
					},{
						type: 'pastel-success',
						delay: 3000,
						template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
							'<span data-notify="title">{1}</span>' +
							'<span data-notify="message">{2}</span>' +
						'</div>'
					});
					getProblem(operation);
				} else {
					$.notify({
						title: 'Incorrect...',
						message: 'Be sure to write the problem down.'
					},{
						type: 'pastel-danger',
						delay: 3000,
						template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
							'<span data-notify="title">{1}</span>' +
							'<span data-notify="message">{2}</span>' +
						'</div>'
					});
				}
			});
		});
	});
}
