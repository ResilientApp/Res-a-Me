<template>
  <div class="m-5">
    <h1 class="mt-4 mb-2 " style="color: white; font-weight: 900;">
      Edit your information here!
      <v-icon
        size="xx-large"
        icon="mdi-pencil"
      ></v-icon>
      <span>
          (Remember to save changes before you leave)
      </span>
    </h1>
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
import { ref, onMounted } from 'vue';
import Skill from '../sections/edit/Skill.vue';
import About from '../sections/edit/About.vue';
import Education from '../sections/edit/Education.vue';
import Profession from '../sections/edit/Profession.vue';
import Certification from '../sections/edit/Certificate.vue';
import Award from '../sections/edit/Award.vue'

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
      name: 'New skill',
      description: 'add your description'
    },
    defaultEdu:{
      id:0,
      diploma: 'New diploma',
      schoolName: 'New shool name',
      startDate: new Date().toISOString().split('T')[0],
      endDate: new Date().toISOString().split('T')[0],
      description: 'add your description'
    },
    defaultPro:{
      id:0,
      position: 'New position',
      company: 'New company name',
      startDate: new Date().toISOString().split('T')[0],
      endDate: new Date().toISOString().split('T')[0],
      description: 'add your description'
    },
    defaultCer:{
      id:0,
      title: 'New certification',
      date: new Date().toISOString().split('T')[0],
      company_school: 'New company name or school name',
      description: 'add your description'
    },
    defaultAward:{
      id:0,
      title: 'New award',
      date: new Date().toISOString().split('T')[0],
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

    onMounted(async () => {
      try {
        //skill data
        const skill_response = await axios.get('../../../data/sections/skills.json');
        const skill_data = skill_response.data;
        // console.log(skill_data)
        const skill_transformedArray = skill_data.items.abilities.map((item, index) => {
          const { faIcon, locales } = item;
          const { title, description } = locales.en;

          return {
            id: index,
            name: title || '',
            description: description || '',
          };
        });
        skills.value = skill_transformedArray;
        //about data
        const cover_response = await axios.get('../../../data/sections/cover.json');
        const cover_data = cover_response.data;
        const profile_response = await axios.get('../../../data/info/profile.json');
        const profile_data = profile_response.data;
        const description = cover_data.locales.en.bio;
        const name = profile_data.name;
        const imgurl = profile_data.profilePictureUrl;
        const position = profile_data.locales.en.role;
        const address = profile_data.contact.address.value;
        const email = profile_data.contact.email.value;
        const phone = profile_data.contact.phone.valueShort;
        const about_transformedArray = {
          name,
          imgurl,
          position,
          description,
          address,
          email,
          phone
        };
        about.value = about_transformedArray
        //education data
        const edu_response = await axios.get('../../../data/sections/education.json');
        const edu_data = edu_response.data;
        const edu_transformedArray = edu_data.items.map((item) => {
          const datePartsS = item.period[0].split('/');
          const yearS = datePartsS[0];
          const monthS = datePartsS[1];
          const dateS = new Date(yearS, monthS - 1);
          const formattedDateS = dateS.toISOString().split('T')[0];
          const datePartsE = item.period[1].split('/');
          const yearE = datePartsE[0];
          const monthE = datePartsE[1];
          const dateE = new Date(yearE, monthE - 1);
          const formattedDateE = dateE.toISOString().split('T')[0];
          return{
              diploma: item.locales.en.title,
              schoolName: item.place.split('{places.')[1].split('}')[0],
              startDate: formattedDateS,
              endDate: formattedDateE,
              description: item.locales.en.description,
          }

        });
        educations.value = edu_transformedArray
        //profession data
        const pro_response = await axios.get('../../../data/sections/experience.json');
        const pro_data = pro_response.data;
        const pro_transformedArray = pro_data.items.map((item) => {
            const datePartsS = item.period[0].split('/');
            const yearS = datePartsS[0];
            const monthS = datePartsS[1];
            const dateS = new Date(yearS, monthS - 1);
            const formattedDateS = dateS.toISOString().split('T')[0];
            const datePartsE = item.period[1].split('/');
            const yearE = datePartsE[0];
            const monthE = datePartsE[1];
            const dateE = new Date(yearE, monthE - 1);
            const formattedDateE = dateE.toISOString().split('T')[0];
            return{
                position: item.locales.en.title,
                company: item.place.split('{places.')[1].split('}')[0],
                startDate: formattedDateS,
                endDate: formattedDateE,
                description: item.locales.en.description,
            }

        });
        professions.value = pro_transformedArray
        //achievement and award data
        const achi_response = await axios.get('../../../data/sections/achievements.json');
        const achi_data = achi_response.data;
        const certificationsArray = achi_data.items.certifications.map((certification) => {
            const dateParts = certification.date.split('/');
            const year = dateParts[0];
            const month = dateParts[1];
            const date = new Date(year, month - 1);
            const formattedDate = date.toISOString().split('T')[0];
            return{
                title: certification.locales.en.title,
                date: formattedDate,
                company_school: certification.place.split('{places.')[1].split('}')[0],
                description: certification.locales.en.description,
            }

        });

        const awardsArray = achi_data.items.awards.map((award) => {
          const dateParts = award.date.split('/');
          const year = dateParts[0];
          const month = dateParts[1];
          // Creating a Date object with the given year and month (subtracting 1 as JS months are zero-indexed)
          const date = new Date(year, month - 1);
          const formattedDate = date.toISOString().split('T')[0];

          return {
            title: award.locales.en.title,
            date: formattedDate,
            company_school: award.place.split('{places.')[1].split('}')[0],
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
      awards
    };
  },
  methods:{
    handleDeleteSkill(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.skills.splice(index, 1); 
          this.skills.forEach((skill, idx) => {
            skill.id = idx;
          });
          console.log("after delete skill:",this.skills) //Post new skills to backend
        }
    },
    handleAddSkill(){
      const addObj = { ...this.defaultSkill };
      addObj.id = this.skills.length;
      this.skills.push(addObj); 
      this.skills.forEach((skill, idx) => {
        skill.id = idx;
      });
      console.log("after add skill:",this.skills); // Post new skills to backend
    },
    handleSaveSkill(skills){
      this.skills = skills;
      console.log("after save skill",this.skills) //Post new skills to backend
    },
    handleSaveAbout(about){
      this.about = Object.assign({}, this.about, about);
      console.log("after save about",this.about) //Post new about to backend
    },
    handleDeleteEdu(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.educations.splice(index, 1); // Modify the educations array in the parent component
          this.educations.forEach((edu, idx) => {
            edu.id = idx;
          });
          console.log("after delete education:",this.educations) //Post new educations to backend
        }
    },
    handleAddEdu(){
      const addObj = { ...this.defaultEdu };
      addObj.id = this.educations.length;
      this.educations.push(addObj); 
      this.educations.forEach((edu, idx) => {
        edu.id = idx;
      });
      console.log("after add education:",this.educations); // Post new educations to backend
    },
    handleSaveEdu(educations){
      this.educations = educations;
      console.log("after save education:",this.educations) //Post new educations to backend
    },
    handleDeletePro(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.professions.splice(index, 1); 
          this.professions.forEach((edu, idx) => {
            edu.id = idx;
          });
          console.log("after delete profession:",this.professions) //Post new professions to backend
        }
    },
    handleAddPro(){
      const addObj = { ...this.defaultPro };
      addObj.id = this.professions.length;
      this.professions.push(addObj); 
      this.professions.forEach((edu, idx) => {
        edu.id = idx;
      });
      console.log("after add profession:",this.professions); // Post new professions to backend
    },
    handleSavePro(professions){
      this.professions = professions;
      console.log("after save profession:",this.professions) //Post new professions to backend
    },
    handleDeleteCer(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.certifications.splice(index, 1); 
          this.certifications.forEach((cer, idx) => {
            cer.id = idx;
          });
          console.log("after delete certification:",this.certifications) //Post new professions to backend
        }
    },
    handleAddCer(){
      const addObj = { ...this.defaultCer };
      addObj.id = this.certifications.length;
      this.certifications.push(addObj); 
      this.certifications.forEach((cer, idx) => {
        cer.id = idx;
      });
      console.log("after add certification:",this.certifications); // Post new certifications to backend
    },
    handleSaveCer(certifications){
      this.certifications = certifications;
      console.log("after save certificate",this.certifications) //Post new certifications to backend
    },
    handleDeleteAward(index){
      if (confirm('Are you sure you want to delete this item?')) {
          this.awards.splice(index, 1); 
          this.awards.forEach((award, idx) => {
            award.id = idx;
          });
          console.log("after delete award:",this.awards) //Post new awards to backend
        }
    },
    handleAddAward(){
      const addObj = { ...this.defaultAward };
      addObj.id = this.awards.length;
      this.awards.push(addObj); 
      this.awards.forEach((award, idx) => {
        award.id = idx;
      });
      console.log("after add award:",this.awards); // Post new awards to backend
    },
    handleSaveAward(awards){
      this.awards = awards;
      console.log("after save award:",this.awards) //Post new awards to backend
    },

  },
  
};

  
</script>

<style>


</style>