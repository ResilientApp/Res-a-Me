<template>
    <v-expansion-panel >
      <v-expansion-panel-title >
        <template v-slot:default="{expanded}">
          <v-row no-gutters class="d-flex jusitfy-start">
            <h1 style="font-weight: 500;">Educational Background</h1>
            <v-icon class="ml-2"
                        size="xx-large"
                        icon="mdi-school-outline"
            ></v-icon>
          </v-row>
        </template>
      </v-expansion-panel-title>
          <v-expansion-panel-text>
            <template v-for="(edu, index) in educations" :key="index">
              <div class="mb-3" style="border:2px solid rgb(198, 194, 194)">
                <v-row no-gutters>
                    <v-col cols="11" >
                      <v-row no-gutters>
                        <v-col cols="3">
                          <v-text-field
                            class="pa-2"
                            v-model="edu.schoolName"
                            :rules="[
                                () => isSchoolnameValid(edu) || 'This field is required'
                            ]"
                            :counter="20"
                            label="School"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="4">
                          <v-text-field
                            class="pa-2"
                            v-model="edu.diploma"
                            :rules="[
                                () => isDiplomaValid(edu) || 'This field is required'
                            ]"
                            :counter="20"
                            label="Diploma"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="edu.startDate"
                            type="date"
                            :counter="10"
                            label="Start Date"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="edu.endDate"
                            type="date"
                            :counter="10"
                            label="End Date"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row no-gutters>
                        <v-text-field
                            class="pl-2 pr-2"
                            v-model="edu.description"
                            :rules="[
                                () => isDescriptionValid(edu)|| 'This field is required'
                            ]"
                            :counter="200"
                            label="Description"
                        ></v-text-field>
                      </v-row>
                    </v-col>
                    <v-col class="button-container mr-2">
                      <v-btn @click="deleteEdu(index)" color="red-lighten-1"
                      > delete
                        <v-icon
                          size="x-large"
                          icon="mdi-trash-can"
                        ></v-icon>
                      </v-btn>
                    </v-col>
                </v-row>
              </div>
            </template>
            <div class="d-flex justify-center">
              <v-btn color="black" @click="addNewEdu()"
                      >Add more
                        <v-icon
                          size="x-large"
                          icon="mdi-plus-thick"
                        ></v-icon>
              </v-btn>
              <v-btn class="ml-5" color="green" @click="saveEdu(educations)"
                      >Save
                        <v-icon 
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
      props: ['educations'],
      
      setup(props,{emit}) {

          watch(() => props.educations, (newEdus, oldEdus) => {
            console.log('New value:', newEdus);
            console.log('Old value:', oldEdus);
          });
          const isSchoolnameValid = (edu) => {
              return !!edu.schoolName;
          };
          const isDiplomaValid = (edu) => {
              return !!edu.diploma;
          };
          const isDescriptionValid = (edu) => {
              return !!edu.description;
          };

          const deleteEdu = (index) => {
            if(index != -1){
              emit('delete-edu',index);
            }
          };
          const addNewEdu = ()=>{
            emit('add-edu');
  
          };
          const saveEdu=(educations)=>{
            let allRulesPassed = true;            
              educations.forEach((edu, index) => {
                if (!isSchoolnameValid(edu) ||
                    !isDiplomaValid(edu) ||
                    !isDescriptionValid(edu)) {
                    allRulesPassed = false;
                }
              });
            if (allRulesPassed) {
                // console.log('data format is correct')
                emit('save-edu', educations);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
          }
  
          return {
            deleteEdu,
            addNewEdu,
            saveEdu,
            isSchoolnameValid,
            isDiplomaValid,
            isDescriptionValid,
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