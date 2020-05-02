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
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        const url = urlParams.get("url");
        if (url) {
            const activity = await axios.get(url).then(response => {
                return response.data;
            })
            this.setActivity(activity);
        }

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

                this.setActivity(data);
            } catch (error) {
                if (error.response.status == 404) {
                    Vue.$toast.error("Je n'ai pas trouvé d'activité :(... En changeant les filtres tu auras peut être plus de chance :)");
                } else {
                    throw error;
                }
            }
        },
        setActivity(data) {
            this.activity = {
                activity: data.activity,
                participants: data.participants,
                type: data.type,
                accessibility: data.accessibility,
                price: data.price,
                link: data.link,
            };
        },
        resetFilters() {
            this.filters.type = "";
            this.filters.participants = "";
            this.filters.price = "";
        }
    },
});