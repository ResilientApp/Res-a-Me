<template>
  <v-expansion-panel >
    <v-expansion-panel-title >
      <template v-slot:default="{expanded}">
        <v-row no-gutters class="d-flex jusitfy-start">
          <h1 style="font-weight: 500;">Skill Set</h1>
          <v-icon class="ml-2"
            size="xx-large"
            icon="mdi-arrow-up-bold-box-outline"
          ></v-icon>
        </v-row>
      </template>
    </v-expansion-panel-title>
        <v-expansion-panel-text>
          <template v-for="(skill, index) in skills" :key="index">
            <div >
              <v-row no-gutters>
                <v-col cols="2">
                  <v-text-field
                    class="pa-2"
                    v-model="skill.title"
                    :rules="[
                        () => !!skill.title || 'This field is required'
                    ]"
                    :counter="20"
                    label="Skill"
                  ></v-text-field>
                </v-col>
                <v-col cols="9">
                  <v-text-field
                    class="pa-2"
                    v-model="skill.description"
                    :rules="[
                        () => !!skill.description || 'This field is required'
                    ]"
                    :counter="200"
                    label="Description"
                  ></v-text-field>
                </v-col>
                <v-col class="button-container">
                    <v-btn @click="deleteSkill(index)" class="mr-2 mb-4"
                    >delete
                      <v-icon color="red"
                        size="x-large"
                        icon="mdi-trash-can"
                      ></v-icon>
                    </v-btn>
                  </v-col>
              </v-row>
            </div>
          </template>
          <div class="d-flex justify-center">
            <v-btn @click="addNew()"
                    >Add more
                      <v-icon
                        size="x-large"
                        icon="mdi-plus-thick"
                      ></v-icon>
            </v-btn>
            <v-btn class="ml-5" @click="saveSkill(skills)"
                    >Save
                      <v-icon color="green"
                        size="x-large"
                        icon="mdi-content-save"
                      ></v-icon>
            </v-btn>
          </div>
        </v-expansion-panel-text>
  </v-expansion-panel>
</template>


<script>
  import { ref, watch, onMounted, toRef } from 'vue';
  export default {
    props: ['skills'],
    
    setup(props,{emit}) {
        // Watch for changes in 'skills' prop
        // watch(() => props.skills, (newSkills, oldSkills) => {
        //   console.log('New value:', newSkills);
        //   console.log('Old value:', oldSkills);
        // });
        const deleteSkill = (index) => {
          if(index != -1){
            emit('delete-skill',index);
          }
        };
        const addNew = ()=>{
          emit('add-skill');

        };
        const saveSkill=(skills)=>{
          
          let allRulesPassed = true;

          skills.forEach((skill, index) => {
            // Check each skill's properties for validation
            if (!skill.title || !skill.description) {
              allRulesPassed = false;
            }
          });

          if (allRulesPassed) {
            // console.log('data is correct')
            emit('save-skill', skills);
          } else {
            confirm('Some fields may be incorrect. Please check!')
          }
        }
        

        return {
          deleteSkill,
          addNew,
          saveSkill
          // Other component logic...
        };
    },

    
  };
</script>


<style>
.button-container {
  display: flex;
  flex-direction: row; /* Vertical layout */
  align-items: center; /* Center items horizontally */
  justify-content: center; /* Center items vertically */
}
</style>