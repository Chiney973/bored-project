export default Vue.component('RandomActivity', {
    name: 'random-activity',
    data: function() {
        return {
            filters: {
                participants: "",
                type: "",
            },
            activity: null,
            activityTypes: [],
            error: "",
        }
    },
    async created() {
        const data = await axios.get("/api/activity-types/")
            .then(response => {
                return response.data
            });
        this.activityTypes = data;
    },
    methods: {
        resetDataActivityAndError() {
            this.activity = null;
            this.error = "";
        },
        forgeFiltersQueryString() {
            return `?participants=${this.filters.participants}&type=${this.filters.type}`;
        },
        async fetchRandomActivity() {
            this.resetDataActivityAndError();

            const filters = this.forgeFiltersQueryString();
            try {
                const data = await axios
                    .get("/api/random-activity" + filters)
                    .then(function(response){
                        return response.data;
                    })

                this.activity = {
                    activity: data.activity,
                    participants: data.participants,
                    type: data.type,
                    accessibility: data.accessibility,
                    price: data.price,
                    link: data.link,
                };
            } catch (error) {
                if (error.response.status == 404) {
                    this.error = "Pas d'activité trouvé :/ Essayez de changer les filtres ?"
                } else {
                    throw error;
                }
            }
        },
        resetFilters() {
            this.filters.type = "";
            this.filters.participants = "";
        }
    },
    template: `
        <div>
            <div>
                <label>Nombre de participants:</label>
                <input v-model=filters.participants placeholder="Peu importe"></input>
                <label>Type</label>
                <select v-model=filters.type>
                    <option
                        v-for="type in activityTypes"
                        :key=type
                        :value=type                        
                    >
                        {{ type }}
                    </option>
                </select>
                <button @click=resetFilters>Raffraichir les filtres</button>
            </div>
            <button @click=fetchRandomActivity>Je tente ma chance</button>
            <div v-if="error">{{error}}</div>
            <div v-if=activity>
            	<div>Activité: {{ activity.activity }}</div>
            	<div>Participants: {{ activity.participants }}</div>
				<div>Catégorie: {{ activity.type }}</div>
				<div>Accéssibilité: {{activity.accessibility}}</div>
				<div>Prix: {{activity.price}}</div>
				<div v-if=activity.link>Lien: {{activity.link}}</div>
            </div>
        </div>
    `
});