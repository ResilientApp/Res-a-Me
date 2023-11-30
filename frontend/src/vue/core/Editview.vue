<template>
  <div class="m-5">
    <v-row>
      <v-col align="center">
        <h1 class="mt-3 mb-3 " style="color: black; font-weight: 900;">
        Edit your information here!
        <v-btn @click="returnButton()" class="ml-5 mb-2">
            <v-icon
              size="xx-large"
              icon="mdi-file-account"
            ></v-icon>
            back to resume
        </v-btn>
        </h1>
      </v-col>
    </v-row>
    
    <v-expansion-panels v-model="panel">
        <About :about="about" @save-about="handleSaveAbout"/>
        <Education :educations="educations" @delete-edu="handleDeleteEdu" @add-edu="handleAddEdu" @save-edu="handleSaveEdu"/>
        <Profession :professions="professions" @delete-pro="handleDeletePro" @add-pro="handleAddPro" @save-pro="handleSavePro"/>
        <Skill :skills="skills" @delete-skill="handleDeleteSkill" @add-skill="handleAddSkill" @save-skill="handleSaveSkill"></Skill>
        <Certification :certifications="certifications" @delete-cer="handleDeleteCer" @add-cer="handleAddCer" @save-cer="handleSaveCer"/>
        <Award :awards="awards" @delete-award="handleDeleteAward" @add-award="handleAddAward" @save-award="handleSaveAward"/>
      </v-expansion-panels>
  </div>
</template>

<script>
import axios from 'axios';
import fs from 'fs'
import { ref, onMounted } from 'vue';
import { useRouter } from "vue-router";
import Skill from '../sections/edit/Skill.vue';
import About from '../sections/edit/About.vue';
import Education from '../sections/edit/Education.vue';
import Profession from '../sections/edit/Profession.vue';
import Certification from '../sections/edit/Certificate.vue';
import Award from '../sections/edit/Award.vue'
const router = useRouter();

export default {
  components: {
    Skill,
    About,
    Education,
    Profession,
    Certification,
    Award,
  },
  data:()=>({
    panel:[0],
    defaultSkill: {
      id: 0,
      title: 'New skill',
      description: 'add your description'
    },
    defaultEdu:{
      id:0,
      title: 'New diploma',
      schoolName: 'New shool name',
      startDate: '2023/01',
      endDate: '2023/12',
      description: 'add your description'
    },
    defaultPro:{
      id:0,
      title: 'New position',
      company: 'New company name',
      startDate: '2023/01',
      endDate: '2023/12',
      description: 'add your description'
    },
    defaultCer:{
      id:0,
      title: 'New certification',
      date: '2023/01',
      company_school: 'New company name or school name',
      description: 'add your description'
    },
    defaultAward:{
      id:0,
      title: 'New award',
      date: '2023/01',
      company_school: 'New company name or school name',
      description: 'add your description'
    },
  }),
  setup() {
    const skills = ref([]);
    const about = ref([]);
    const educations = ref([]);
    const professions = ref([]);
    const certifications = ref([]);
    const awards = ref([]);
    const cover_data_old = ref([]);
    const profile_data_old = ref([]);
    const skill_data_old = ref([]);
    const edu_data_old = ref([]);
    const pro_data_old = ref([]);
    const achi_data_old = ref([]);

    onMounted(async () => {
      try {
        //skill data
        // const skill_response = await axios.get('../../../data/sections/skills.json');
        // const skill_data = skill_response.data;
        const skill_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "skills"}),
            });
        const skill_data = await skill_response.json();
        skill_data_old.value = skill_data; //for update JSON file
        const skill_transformedArray = skill_data.items.abilities.map((item, index) => {
          const { faIcon, locales } = item;
          const { title, description } = locales.en;

          return {
            id: index,
            title: title || '',
            description: description || '',
          };
        });
        skills.value = skill_transformedArray;
        //about data
        // const cover_response = await axios.get('../../../data/sections/cover.json');
        // const cover_data = cover_response.data;
        const cover_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "cover"}),
            });
        const cover_data = await cover_response.json();
        cover_data_old.value = cover_data; //for update JSON file
        const profile_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "profile"}),
            });
        const profile_data = await profile_response.json();
        // const profile_response = await axios.get('../../../data/info/profile.json');
        // const profile_data = profile_response.data;
        profile_data_old.value = profile_data;
        const description = cover_data.locales.en.bio;
        const name = profile_data.name;
        const profilePictureUrl = profile_data.profilePictureUrl;
        const role = profile_data.locales.en.role;
        const address = profile_data.contact.address.value;
        const email = profile_data.contact.email.value;
        const phone = profile_data.contact.phone.valueShort;
        const about_transformedArray = {
          name,
          profilePictureUrl,
          role,
          description,
          address,
          email,
          phone
        };
        about.value = about_transformedArray
        //education data
        // const edu_response = await axios.get('../../../data/sections/education.json');
        // const edu_data = edu_response.data;
        const edu_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "education"}),
            });
        const edu_data = await edu_response.json();
        edu_data_old.value = edu_data; //for update JSON file
        const edu_transformedArray = edu_data.items.map((item) => {
          return{
              title: item.locales.en.title,
              schoolName: item.place, 
              startDate: item.period[0],
              endDate: item.period[1],
              description: item.locales.en.description,
          }

        });
        educations.value = edu_transformedArray
        //profession data
        // const pro_response = await axios.get('../../../data/sections/experience.json');
        // const pro_data = pro_response.data;
        const pro_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "experience"}),
            });
        const pro_data = await pro_response.json();
        pro_data_old.value = pro_data; //for update JSON file
        const pro_transformedArray = pro_data.items.map((item) => {
            return{
                title: item.locales.en.title,
                company: item.place, 
                startDate: item.period[0],
                endDate: item.period[1],
                description: item.locales.en.description,
            }

        });
        professions.value = pro_transformedArray
        //achievement and award data
        // const achi_response = await axios.get('../../../data/sections/achievements.json');
        // const achi_data = achi_response.data;
        const achi_response = await fetch("http://127.0.0.1:3033/loadResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "achievements"}),
            });
        const achi_data = await achi_response.json();
        achi_data_old.value = achi_data; //for update JSON file
        const certificationsArray = achi_data.items.certifications.map((certification) => {
            return{
                title: certification.locales.en.title,
                date: certification.date,
                company_school: certification.place, 
                description: certification.locales.en.description,
            }
        });
        const awardsArray = achi_data.items.awards.map((award) => {
          return {
            title: award.locales.en.title,
            date: award.date,
            company_school: award.place, 
            description: award.locales.en.description,
          };
        });
        certifications.value = certificationsArray
        awards.value = awardsArray
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    });
    
    return {
      skills,
      about,
      educations,
      professions,
      certifications,
      awards,
      cover_data_old,
      profile_data_old,
      skill_data_old,
      edu_data_old,
      pro_data_old,
      achi_data_old,
    };
  },
  methods:{
    returnButton(){
      if(confirm('Are you sure you want to leave this page? Make sure you have saved your changes!')){
        this.$router.push('/home');
      }
    },
    handleDeleteSkill(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.skills.splice(index, 1); 
          this.skills.forEach((skill, idx) => {
            skill.id = idx;
          });
        }
    },
    handleAddSkill(){
      const addObj = { ...this.defaultSkill };
      addObj.id = this.skills.length;
      this.skills.push(addObj); 
      this.skills.forEach((skill, idx) => {
        skill.id = idx;
      });
    },
    handleSaveSkill(skills){
      this.skills = skills;
      this.skill_data_old.items.abilities = [];
      for (let i = 0; i < this.skills.length; i++) {
        const extractedItem = this.skills[i];
        this.skill_data_old.items.abilities.push({
          imageIconUrl: null,
          faIcon: null,
          value: null,
          locales: {
            en: {
              title: extractedItem.title || '',
              description: extractedItem.description || ''
            },
            es: { title: '', description: '' },
            fr: { title: '', description: '' },
            zh: { title: '', description: '' }
          }
        });
      }
      const skill_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "skills","data": JSON.stringify(this.skill_data_old)}),
            });
    },
    handleSaveAbout(about){
      this.about = Object.assign({}, this.about, about);
      this.cover_data_old.locales.en.bio = this.about.description;
      this.profile_data_old.name = this.about.name;
      this.profile_data_old.profilePictureUrl = this.about.profilePictureUrl;
      this.profile_data_old.locales.en.role = this.about.role;
      this.profile_data_old.contact.address.value = this.about.address;
      this.profile_data_old.contact.email.value = this.about.email;
      this.profile_data_old.contact.phone.valueShort = this.about.phone;
      const cover_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "cover","data": JSON.stringify(this.cover_data_old)}),
      });
    
      const profile_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "profile","data": JSON.stringify(this.profile_data_old)}),
      });
      // console.log("cover_data",this.cover_data_old) //Post new about to backend
      // console.log("profile_data",this.profile_data_old) //Post new about to backend
    },
    handleDeleteEdu(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.educations.splice(index, 1); // Modify the educations array in the parent component
          this.educations.forEach((edu, idx) => {
            edu.id = idx;
          });
        }
    },
    handleAddEdu(){
      const addObj = { ...this.defaultEdu };
      addObj.id = this.educations.length;
      this.educations.push(addObj); 
      this.educations.forEach((edu, idx) => {
        edu.id = idx;
      });
    },
    handleSaveEdu(educations){
      this.educations = educations;
      // Clear existing items in edu_data
      this.edu_data_old.items = [];
      for (let i = 0; i < this.educations.length; i++) {
        const extractedItem = this.educations[i];
        this.edu_data_old.items.push({
              id: extractedItem.id,
              place: extractedItem.schoolName || '',
              period: [extractedItem.startDate || '', extractedItem.endDate || ''],
              locales: {
                  en: {
                      title: extractedItem.title || '',
                      description: extractedItem.description || '',
                  },
                  es: { title: '', description: '' },
                  fr: { title: '', description: '' },
                  zh: { title: '', description: '' },
              },
        });
      }
      const edu_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "education","data": JSON.stringify(this.edu_data_old)}),
            });
    },
    handleDeletePro(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.professions.splice(index, 1); 
          this.professions.forEach((edu, idx) => {
            edu.id = idx;
          });
        }
    },
    handleAddPro(){
      const addObj = { ...this.defaultPro };
      addObj.id = this.professions.length;
      this.professions.push(addObj); 
      this.professions.forEach((edu, idx) => {
        edu.id = idx;
      });
    },
    handleSavePro(professions){
      this.professions = professions;
      this.pro_data_old.items = [];
      for (let i = 0; i < this.professions.length; i++) {
        const extractedItem = this.professions[i];
        this.pro_data_old.items.push({
              id: extractedItem.id,
              place: extractedItem.company || '',
              period: [extractedItem.startDate || '', extractedItem.endDate || ''],
              locales: {
                  en: {
                      title: extractedItem.title || '',
                      description: extractedItem.description || '',
                  },
                  es: { title: '', description: '' },
                  fr: { title: '', description: '' },
                  zh: { title: '', description: '' },
              },
        });
      }
      const pro_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "experience","data": JSON.stringify(this.pro_data_old)}),
            });
    },
    handleDeleteCer(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.certifications.splice(index, 1); 
          this.certifications.forEach((cer, idx) => {
            cer.id = idx;
          });
        }
    },
    handleAddCer(){
      const addObj = { ...this.defaultCer };
      addObj.id = this.certifications.length;
      this.certifications.push(addObj); 
      this.certifications.forEach((cer, idx) => {
        cer.id = idx;
      });
    },
    handleSaveCer(certifications){
      this.certifications = certifications;
      this.achi_data_old.items.certifications = [];
      for (let i = 0; i < this.certifications.length; i++) {
        const extractedItem = this.certifications[i];
        this.achi_data_old.items.certifications.push({
              id: extractedItem.id,
              place: extractedItem.company_school || '',
              date: extractedItem.date || '',
              href: '',
              locales: {
                  en: {
                      title: extractedItem.title || '',
                      description: extractedItem.description || '',
                  },
                  es: { title: '', description: '' },
                  fr: { title: '', description: '' },
                  zh: { title: '', description: '' },
              },
        });
      }
      const achi_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "achievements","data": JSON.stringify(this.achi_data_old)}),
            });
    },
    handleDeleteAward(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.awards.splice(index, 1); 
          this.awards.forEach((award, idx) => {
            award.id = idx;
          });
        }
    },
    handleAddAward(){
      const addObj = { ...this.defaultAward };
      addObj.id = this.awards.length;
      this.awards.push(addObj); 
      this.awards.forEach((award, idx) => {
        award.id = idx;
      });
    },
    handleSaveAward(awards){
      this.awards = awards;
      this.achi_data_old.items.awards = [];
      for (let i = 0; i < this.awards.length; i++) {
        const extractedItem = this.awards[i];
        this.achi_data_old.items.awards.push({
              id: extractedItem.id,
              place: extractedItem.company_school || '',
              date: extractedItem.date || '',
              href: '',
              locales: {
                  en: {
                      title: extractedItem.title || '',
                      description: extractedItem.description || '',
                  },
                  es: { title: '', description: '' },
                  fr: { title: '', description: '' },
                  zh: { title: '', description: '' },
              },
        });
      }
      const achi_response = fetch("http://127.0.0.1:3033/editResume", {
                method: "POST",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                },
                body :JSON.stringify({"category": "acheivements","data": JSON.stringify(this.achi_data_old)}),
            });
    },

  },
  
};

  
</script>

<style>

/* #app{
  background-color: ivory !important
} */
</style>
