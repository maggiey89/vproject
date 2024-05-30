<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card>
            <!-- <v-card-title>近期數據列表</v-card-title> -->
            <v-card-text>
              <v-data-table
                :headers="headers"
                :items="recentData"
                :items-per-page="5"
                class="elevation-1"
              >
                <template v-slot:items="props">
                  <td>{{ props.item.date }}</td>
                  <td>{{ props.item.value }}</td>
                </template>
              </v-data-table>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        headers: [
          { text: '日期', value: 'date' },
          { text: '數據值', value: 'value' }
        ],
        recentData: [
          { date: '2024-03-01', value: 100 },
          { date: '2024-03-02', value: 150 },
          { date: '2024-03-03', value: 120 },
          { date: '2024-03-04', value: 130 },
          { date: '2024-03-05', value: 200 }
        ]
      };
    }
  };
  </script>
  
