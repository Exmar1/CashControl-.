document.addEventListener('DOMContentLoaded', function() {
	// Подсветка активного поля ввода
	const inputFields = document.querySelectorAll('.form-group input');
	
	inputFields.forEach(field => {
			field.addEventListener('focus', function() {
					this.parentElement.classList.add('active');
			});
			
			field.addEventListener('blur', function() {
					this.parentElement.classList.remove('active');
			});
	});
	
	// Автоматическое скрытие сообщений об ошибках через 5 секунд
	const errorMessages = document.querySelectorAll('.error-message');
	
	if (errorMessages.length > 0) {
			setTimeout(() => {
					errorMessages.forEach(message => {
							message.style.opacity = '0';
							setTimeout(() => {
									message.style.display = 'none';
							}, 300);
					});
			}, 5000);
	}
});