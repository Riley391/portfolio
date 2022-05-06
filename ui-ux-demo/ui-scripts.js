class Plant {
    constructor(name, latin, family, genus, edible, edibleParts, category, description, image, link) {
        this.name = name;
        this.latin = latin;
        this.family = family;
        this.genus = genus;
        this.edible = edible;
        this.edibleParts = edibleParts;
        this.category = category;
        this.description = description;
        this.image = image;
        this.link = link;
    }

    getData() {
        return { 
            name: this.name, 
            latin: this.latin, 
            family: this.family, 
            genus: this.genus, 
            edible: this.edible, 
            edibleParts: this.edibleParts, 
            category: this.category, 
            description: this.description, 
            image: this.image,
            link: this.link
        }
    }
}

// TODO: add link css to populatePlants and NOT to populatePlant
function populatePlants(plants) {
    let plantDivs = [];
    for (i = 0; i < plants.length; i++) {
        const plantLink = document.createElement("a");
        plantLink.href = plants[i].link;

        const plantSpan = document.createElement("span");
        plantSpan.className = "link";

        const plantDiv = document.createElement("div");
        plantDiv.className = "plant";
        plantDiv.innerHTML = plants[i].name;
        plantDiv.style.backgroundImage = `url(${plants[i].image})`;

        plantDiv.appendChild(plantLink);
        plantLink.appendChild(plantSpan);
        plantDivs.push(plantDiv);
    }
    for (let plantDiv of plantDivs) {
        document.getElementById('plantBox').appendChild(plantDiv);
    }
}

function populatePlant(plant) {
    const plantDiv = document.createElement("div");
    plantDiv.className = "plant";
    plantDiv.innerHTML = plant.name;
    plantDiv.style.backgroundImage = `url(${plant.image})`;
    plantDiv.style.height = '400px';
    plantDiv.style.width = '800px';

    document.getElementById('plantBox').appendChild(plantDiv);
}

califHazel = new Plant('California Hazel', 'corylus cornuta var. californica', 'Betulaceae', 'Corylus', true, ['nut'], 'shrub', 
    'The California Hazel is a large shrub native to the western coast of North America. \
    It produces nuts which are almost identical to hazelnuts, and it can also be grown as a pleasing bonsai.', 'images/california-hazel.png', 'california-hazel.html');

blackNightshade = new Plant('Black Nightshade', 'solanum nigrum', 'Solanaceae', 'Solanum', false, [], 'herb', 
    'Black Nightshade is a small flowering plant which produces toxic berries. It is native to Europe but has now been \
    naturalized in much of North America. Though it is in the same family as potatoes and tomatoes, the berries of the \
    black nightshade plant can cause fever, gastrointestinal distress, and in rare cases, death.', 'images/black-nightshade.jpg', 'black-nightshade.html');

califHazel1 = new Plant('California Hazel', 'corylus cornuta var. californica', 'Betulaceae', 'Corylus', true, ['nut'], 'shrub', 
    'The California Hazel is a large shrub native to the western coast of North America. \
    It produces nuts which are almost identical to hazelnuts, and it can also be grown as a pleasing bonsai.', 'images/california-hazel.png', 'california-hazel.html');

blackNightshade1 = new Plant('Black Nightshade', 'solanum nigrum', 'Solanaceae', 'Solanum', false, [], 'herb', 
    'Black Nightshade is a small flowering plant which produces toxic berries. It is native to Europe but has now been \
    naturalized in much of North America. Though it is in the same family as potatoes and tomatoes, the berries of the \
    black nightshade plant can cause fever, gastrointestinal distress, and in rare cases, death.', 'images/black-nightshade.jpg', 'black-nightshade.html');

const plants = [califHazel, blackNightshade, califHazel1, blackNightshade1];