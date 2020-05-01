new Vue({
    el: '#random-activity',
    delimiters: [ "[[", "]]" ],
    data: function() {
        return {
            filters: {
                participants: "",
                type: "",
                price: "",
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
            return `?participants=${this.filters.participants}&type=${this.filters.type}&price=${this.filters.price}`;
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
                    this.error = "Je n'ai pas trouvé d'activité :(... En changeant les filtres vous aurez peut être plus de chance :)"
                } else {
                    throw error;
                }
            }
        },
        resetFilters() {
            this.filters.type = "";
            this.filters.participants = "";
            this.filters.price = "";
        }
    },
});