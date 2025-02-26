// static/finance/js/transactions.js
document.addEventListener('DOMContentLoaded', function() {
	// Инициализация выбора даты с помощью Flatpickr
	const datePickerOptions = {
			dateFormat: "Y-m-d",
			locale: "ru",
			allowInput: true,
			altFormat: "d.m.Y",
	};
	
	flatpickr(".date-picker", datePickerOptions);

	// Сброс фильтров
	document.getElementById('reset-filters').addEventListener('click', function() {
			const form = document.getElementById('filters-form');
			
			// Очистка всех полей формы
			form.querySelectorAll('input, select').forEach(input => {
					if (input.type === 'text' || input.type === 'number') {
							input.value = '';
					} else if (input.tagName === 'SELECT') {
							input.selectedIndex = 0;
					}
			});
			
			// Отправка формы
			form.submit();
	});

	// Анимация для таблицы
	const tableRows = document.querySelectorAll('.transactions-table tbody tr');
	tableRows.forEach((row, index) => {
			row.style.opacity = '0';
			row.style.transform = 'translateY(10px)';
			row.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
			setTimeout(() => {
					row.style.opacity = '1';
					row.style.transform = 'translateY(0)';
			}, 50 * index);
	});
});

// Функция для редактирования транзакции (заглушка, можно реализовать позже)
function editTransaction(id) {
	alert('Функция редактирования транзакции будет добавлена позже. ID транзакции: ' + id);
	// Здесь можно реализовать открытие модального окна для редактирования
}