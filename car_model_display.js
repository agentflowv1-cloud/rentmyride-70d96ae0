class CarModelDisplay {
  constructor(homepageElement) {
    this.homepageElement = homepageElement;
    this.carModels = [];
    this.filteredCarModels = [];
    this.init();
  }

  init() {
    this.loadCarModels();
    this.renderCarModels();
    this.addEventListeners();
  }

  loadCarModels() {
    // Load car models from API or database
    // For demonstration purposes, using mock data
    this.carModels = [
      { id: 1, type: 'Sedan', location: 'New York', rating: 4.5 },
      { id: 2, type: 'SUV', location: 'Los Angeles', rating: 4.2 },
      { id: 3, type: 'Truck', location: 'Chicago', rating: 4.8 }
    ];
  }

  renderCarModels() {
    const carModelsHTML = this.carModels.map((carModel) => {
      return `<div class='car-model'>
        <h2>${carModel.type}</h2>
        <p>Location: ${carModel.location}</p>
        <p>Rating: ${carModel.rating}/5</p>
        <button class='view-details'>View Details</button>
      </div>`;
    }).join('');
    this.homepageElement.innerHTML = carModelsHTML;
  }

  addEventListeners() {
    const viewDetailsButtons = this.homepageElement.querySelectorAll('.view-details');
    viewDetailsButtons.forEach((button) => {
      button.addEventListener('click', (e) => {
        const carModelId = e.target.parentNode.querySelector('h2').textContent;
        // Navigate to car model details page or display details in a modal
      });
    });
  }

  filterCarModels(filterType, filterValue) {
    this.filteredCarModels = this.carModels.filter((carModel) => {
      if (filterType === 'type') return carModel.type === filterValue;
      if (filterType === 'location') return carModel.location === filterValue;
      if (filterType === 'rating') return carModel.rating >= filterValue;
    });
    this.renderCarModels(this.filteredCarModels);
  }
}

// Example usage
const homepageElement = document.getElementById('homepage');
const carModelDisplay = new CarModelDisplay(homepageElement);
