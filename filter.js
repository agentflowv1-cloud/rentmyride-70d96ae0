class Filter {
  constructor(filterElement) {
    this.filterElement = filterElement;
    this.filterType = '';
    this.filterValue = '';
    this.init();
  }

  init() {
    this.addEventListeners();
  }

  addEventListeners() {
    const filterSelect = this.filterElement.querySelector('select');
    filterSelect.addEventListener('change', (e) => {
      this.filterType = e.target.value;
      this.filterValue = this.filterElement.querySelector('input').value;
      // Call filterCarModels method on CarModelDisplay instance
    });
  }
}

// Example usage
const filterElement = document.getElementById('filter');
const filter = new Filter(filterElement);
