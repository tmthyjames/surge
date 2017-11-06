var getProblem = function(grade, operation){
	var types = ['simple_word', 'nonword']
	var type = types[Math.floor(Math.random()*types.length)];
	var endpoint = '/api/generate/' + grade + "/" + type + '/' + operation;
	var random = window.location.href.indexOf('random');
	if (random >= 0){
		operations = ['addition', 'subtraction'];
		operation = operations[Math.floor(Math.random()*operations.length)];
		endpoint = '/api/generate/' + grade + "/" + type + '/' + operation
	}

	$.get(endpoint, function(d){
		$('#problem').html(
			d.text
			+ '<div class="row">'
			  + '<div class="col-lg-6">'
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
			var answer = $('#answer').val().trim() || '0';
			var terms = d.problem.terms;
			var checkEndPoint;
			if (type == 'simple_word'){
				checkEndPoint = '/api/check/' + grade + "/" + type + "/" + operation + "/" + answer + "/" + d.problem.answer + "/?problem="+d.problem.problem;
			} else {
				checkEndPoint = '/api/check/' + grade + "/" + type + '/' + operation + '/' + terms[0] + '/' + terms[1] + '/' + answer + "/";
			}
			$.get(checkEndPoint, function(data){
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
					getProblem(grade, operation);
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
