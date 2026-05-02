document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const table = document.querySelector('table');

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const day = document.querySelector('input[name="day"]:checked');
    if (!day) return;
    const colIndex = { 'mon':1, 'tue':2, 'wed':3, 'thu':4, 'fri':5, 'sat':6 }[day.value];

    const paras = document.querySelectorAll('input[name="para"]:checked');
    if (!paras.length) return;

    const subject = document.querySelector('input[type="text"]').value.trim();
    const select = document.querySelector('select');
    const type = select.options[select.selectedIndex].text.trim();

    let cellText = subject;
    if (subject !== '' && type !== 'Тип') {cellText = subject + ' (' + type + ')';}

    paras.forEach(cb => {const row = table.rows[parseInt(cb.value)];
      if (row && row.cells[colIndex]) {row.cells[colIndex].textContent = cellText;}
    });
  });
});