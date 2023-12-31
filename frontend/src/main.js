/**
 * Created by Ryan Balieiro on 08.23.2023
 * App's entry point
 */
import './scss/style.scss'
import {useData} from "./composables/data.js"
import {useLanguage} from "./composables/language.js"
import {useNavigation} from "./composables/navigation.js"
import {createAppRouter} from "./router/router.js"
import {createApp} from "vue"
import App from './vue/core/App.vue'

import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import * as components from 'vuetify/components'
import "@mdi/font/css/materialdesignicons.css";


import '@mdi/font/css/materialdesignicons.css'

const data = useData()
// const eventBus = mitt()

data.fetchEssentials().then(r => {
    const language = useLanguage()
    language.init(data.getSettings()['supportedLanguages'])

    const navigation = useNavigation()
    navigation.init(data.getSections(), data.getCategories())

    const router = createAppRouter()
    const vuetify = createVuetify({
        components,
    })
    createApp(App).use(router).use(vuetify).mount('#app')
})