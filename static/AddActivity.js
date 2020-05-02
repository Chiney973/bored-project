new Vue({
    el: '#add-activity',
    delimiters: [ "[[", "]]" ],
    data: function() {
        return {
            form: {
                activity: null,
                accessibility: null,
                type: null,
                participants: null,
                price: null,
                link: null,
            },
            error: "",
        }
    },
    methods: {
        cleanForm() {
            const cleanedForm = {...this.form};
            for (const key in cleanedForm){
                if (cleanedForm[key] == null) {
                    delete cleanedForm[key];
                }
            }
            return cleanedForm;
        },
        async createActivity() {
            
            const data = this.cleanForm();
            try {
                const response = await axios.post(
                    "/api/activities/",
                    data,
                    {headers: {"Content-type": "application/json"}},
                ).then(response => {
                    return response.data;
                });

                const url = encodeURI(response.url);
                window.location.href = `/?url=${url}`
                
            } catch (error) {
                Vue.$toast.error("Echec de l'ajout de l'activité :/ As tu bien rempli le formulaire ?");
                console.log(error.response);
            }
        }
    },
});