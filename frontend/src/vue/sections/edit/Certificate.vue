<template>
    <v-expansion-panel >
      <v-expansion-panel-title >
        <template v-slot:default="{expanded}">
          <v-row no-gutters class="d-flex jusitfy-start">
            <h1 style="font-weight: 500;">Certification</h1>
            <v-icon class="ml-2"
                        size="xx-large"
                        icon="mdi-certificate-outline"
            ></v-icon>
          </v-row>
        </template>
      </v-expansion-panel-title>
          <v-expansion-panel-text>
            <template v-for="(certifi, index) in certifications" :key="index">
              <div class="mb-3" style="border:2px solid rgb(198, 194, 194)">
                <v-row no-gutters>
                    <v-col cols="11" >
                      <v-row no-gutters>
                        <v-col cols="3">
                          <v-text-field
                            class="pa-2"
                            v-model="certifi.title"
                            :rules="[
                                () => isTitleValid(certifi) || 'This field is required'
                            ]"
                            :counter="40"
                            label="Title"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="4">
                          <v-text-field
                            class="pa-2"
                            v-model="certifi.date"
                            :rules="[
                                () => !!certifi.date || 'This field is required',
                                () => isDateValid(certifi) || 'Date must be in YYYY/MM format'
                            ]"
                            :counter="20"
                            label="Date"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="certifi.company_school"
                            :rules="[
                                () => isCompanySchoolValid(certifi) || 'This field is required'
                            ]"
                            :counter="10"
                            label="Company/School"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row no-gutters>
                        <v-text-field
                            class="pl-2 pr-2"
                            v-model="certifi.description"
                            :rules="[
                                () => isDescriptionValid(certifi)|| 'This field is required'
                            ]"
                            :counter="200"
                            label="Description"
                        ></v-text-field>
                      </v-row>
                    </v-col>
                    <v-col class="button-container">
                      <v-btn @click="deleteCer(index)" color="red-lighten-2"
                      >
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
              <v-btn color="grey-lighten-1" @click="addNewCer()"
                      >Add more
                        <v-icon
                          size="x-large"
                          icon="mdi-plus-thick"
                        ></v-icon>
              </v-btn>
              <v-btn class="ml-5" color="green" @click="saveCer(certifications)"
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
      props: ['certifications'],
      
      setup(props,{emit}) {

          // watch(() => props.certifications, (newCers, oldCers) => {
          //   console.log('New value:', newCers);
          //   console.log('Old value:', oldCers);
          // });
          const isTitleValid = (certifi) => {
              return !!certifi.title;
          };
          const isCompanySchoolValid = (certifi) => {
              return !!certifi.company_school;
          };
          const isDateValid = (certifi) => {
              return !!certifi.date && /\b\d{4}\/(0[1-9]|1[0-2])\b/.test(certifi.date);;
          };
          const isDescriptionValid = (edu) => {
              return !!edu.description;
          };

          const deleteCer = (index) => {
            if(index != -1){
              emit('delete-cer',index);
            }
          };
          const addNewCer = ()=>{
            emit('add-cer');
  
          };
          const saveCer=(certifications)=>{
            let allRulesPassed = true;            
            certifications.forEach((cer, index) => {
                if (!isTitleValid(cer) ||
                    !isCompanySchoolValid(cer) ||
                    !isDateValid(cer) ||
                    !isDescriptionValid(cer)) {
                    allRulesPassed = false;
                }
              });
            if (allRulesPassed) {
                // console.log('data format is correct')
                alert('Your Certificate information has been saved!')
                emit('save-cer', certifications);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
          }
  
          return {
            deleteCer,
            addNewCer,
            saveCer,
            isTitleValid,
            isCompanySchoolValid,
            isDescriptionValid,
            isDateValid
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