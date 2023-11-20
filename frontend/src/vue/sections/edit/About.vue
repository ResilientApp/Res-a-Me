<template>
    <v-expansion-panel>
        <v-expansion-panel-title>
          <template v-slot:default="{expanded}">
              <v-row no-gutters class="d-flex jusitfy-start ">
                    <h1 style="font-weight: 500;">
                        About
                    </h1>
                    <v-icon class="ml-2"
                        size="xx-large"
                        icon="mdi-information-outline"
                    ></v-icon>
              </v-row>
          </template>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
            <v-row no-gutters>
                <v-col>
                    <v-text-field class="pa-2"
                    v-model="about.name"
                    :rules="[
                        () => !!about.name || 'This field is required',
                        () => isNameValid() || 'Name must be at least 2 characters and less than 20 characters'
                    ]"
                    :counter="20"
                    label="Name"
                    ></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field class="pa-2"
                    v-model="about.position"
                    :rules="[
                        () => !!about.position || 'This field is required',
                        () => isPositionValid() || 'Position must be at least 2 characters and less than 20 characters'
                    ]"
                    :counter="20"
                    label="Job Title"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters>
                <v-col>
                    <v-text-field class="pa-2"
                    v-model="about.address"
                    :rules="[
                        () => !!about.address || 'This field is required',
                        () => isAddressValid() || 'Address must be less than 50 characters'
                    ]"
                    :counter="50"
                    label="Address"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters>
                <v-col>
                    <v-text-field class="pa-2"
                    v-model="about.phone"
                    :rules="[
                        () => !!about.phone || 'This field is required',
                        () => isPhoneValid() || 'Phone must be in (XXX) XXX-XXXX format'
                    ]"
                    :counter="15"
                    label="Phone Number"
                    ></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field class="pa-2"
                    v-model="about.email"
                    :rules="[
                        () => !!about.email || 'This field is required',
                        () => isEmailValid() || 'Email must be in the correct format'
                    ]"
                    :counter="30"
                    label="E-mail"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters>
                <v-text-field class="pa-2"
                    v-model="about.description"
                    :rules="[
                        () => !!about.description || 'This field is required',
                        () =>  isDescriptionValid() || 'Introduction must be less than 250 characters'
                    ]"
                    :counter="250"
                    label="Introduction"
                    ></v-text-field>
            </v-row>
            <div class="d-flex justify-center">
                <v-btn class="ml-5" @click="saveAbout(about)"
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
import { ref, watch, computed} from 'vue';
export default {
    props:["about"],
    
    setup(props,{emit}) {
        // Watch for changes in 'skills' prop
        // watch(() => props.about, (newAbout, oldAbout) => {
        //   console.log('New value:', newAbout);
        //   console.log('Old value:', oldAbout);
        // });
        const isNameValid = () => {
            return !!props.about.name && props.about.name.length >= 2 && props.about.name.length <= 20;
        };
        const isPositionValid = () => {
            return !!props.about.position && props.about.position.length >= 2 && props.about.position.length <= 20;
        };
        const isAddressValid = () => {
            return !!props.about.address && props.about.address.length <= 50;
        };
        const isPhoneValid = () => {
            return !!props.about.phone && /^\(\d{3}\)\s\d{3}-\d{4}$/.test(props.about.phone);
        };
        const isEmailValid = () => {
            return (
                !!props.about.email &&
                /^[a-z0-9][-a-z0-9._]+@([-a-z0-9]+.)+[a-z]{2,5}$/.test(props.about.email)
            );
        };
        const isDescriptionValid = () => {
            return !!props.about.description && props.about.description.length <= 250;
        };
        const saveAbout=(about)=>{

            let allRulesPassed = true;
            if (!isNameValid() ||
                !isPositionValid() ||
                !isAddressValid() ||
                !isPhoneValid() ||
                !isEmailValid() ||
                !isDescriptionValid()) {
                allRulesPassed = false;
            }

            if (allRulesPassed) {
                console.log('data format is correct')
                emit('save-about', about);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
        }
        

        return {
          saveAbout,
          isNameValid,
          isPositionValid,
          isAddressValid,
          isPhoneValid,
          isEmailValid,
          isDescriptionValid,
        };
    },
    
}
</script>

<style>

</style>


