<template>
  <section class="bg-white dark:bg-gray-900" aria-labelledby="family-models-title">
    <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
      <h2 id="family-models-title" class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-3">
        {{ t(family.title) }}
      </h2>
      <p v-if="family.intro" class="text-base md:text-lg text-[#444545] dark:text-gray-300 leading-relaxed max-w-[72ch] mb-6">{{ t(family.intro) }}</p>

      <!-- Type selector: only when the family has more than one type -->
      <div v-if="types.length > 1" role="group" :aria-label="isAr ? 'نوع الباب' : 'Door type'" class="grid grid-cols-2 lg:grid-cols-5 gap-3 mb-8">
        <button
          v-for="tp in types"
          :key="tp.id"
          type="button"
          :aria-pressed="tp.id === current.id ? 'true' : 'false'"
          class="text-start rounded-xl px-4 py-3.5 bg-white dark:bg-gray-800 transition flex flex-col gap-1 min-h-[44px]"
          :class="tp.id === current.id
            ? 'border-2 border-[#191919] dark:border-[#E99E05] shadow-[inset_0_-4px_0_#E99E05]'
            : 'border border-[#A9AAAA] dark:border-gray-600 hover:border-[#191919]'"
          @click="typeId = tp.id"
        >
          <span class="font-display font-bold text-base md:text-lg text-[#191919] dark:text-white">{{ t(tp.label) }}</span>
          <span v-if="tp.key" class="text-sm text-[#444545] dark:text-gray-300 leading-snug">{{ t(tp.key) }}</span>
          <span class="text-xs text-[#5E5F5F] dark:text-gray-400">{{ countLabel(tp.models.length) }}</span>
        </button>
      </div>

      <h3 v-if="types.length > 1" class="font-display text-xl md:text-2xl font-bold text-[#191919] dark:text-white mb-2">
        {{ t(current.label) }}{{ isAr ? ': المواصفات والمقارنة' : ': specifications and comparison' }}
      </h3>
      <p v-if="current.intro" class="text-base md:text-lg text-[#444545] dark:text-gray-300 leading-relaxed max-w-[72ch] mb-5">{{ t(current.intro) }}</p>

      <!-- Desktop / tablet: comparison table -->
      <div class="hidden md:block bp overflow-x-auto">
        <table :style="{ minWidth: (190 + current.models.length * 210) + 'px' }">
          <caption class="text-start px-4 py-2.5 text-sm text-[#5E5F5F] dark:text-gray-400 border-b border-[#191919] dark:border-gray-600">{{ t(family.source) }}</caption>
          <thead>
            <tr>
              <th scope="col" class="w-[190px]">{{ isAr ? 'البند' : 'Item' }}</th>
              <th v-for="m in current.models" :key="m.code" scope="col" :id="anchor(m)" class="whitespace-normal align-top">
                {{ t(m.name) }}
                <span class="block font-normal text-xs text-[#5E5F5F] dark:text-gray-400 mt-1"><bdi>{{ m.code }}</bdi> · {{ t(m.origin) }}</span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in rowsFor(current)" :key="row.key">
              <th scope="row" class="font-bold text-[#191919] dark:text-white">{{ t(row.label) }}</th>
              <td v-for="m in current.models" :key="m.code" class="bp-num text-[#333434] dark:text-gray-200 align-top">
                <bdi v-if="has(m, row.key)" :dir="isAr ? 'rtl' : 'ltr'">{{ cell(m, row.key) }}</bdi>
                <span v-else class="text-[#6F7070] dark:text-gray-400">{{ isAr ? 'عند الطلب' : 'On request' }}</span>
              </td>
            </tr>
            <tr>
              <th scope="row" class="font-bold text-[#191919] dark:text-white">{{ isAr ? 'الطلب' : 'Request' }}</th>
              <td v-for="m in current.models" :key="m.code">
                <button type="button" class="min-h-[44px] px-4 rounded-lg border border-[#191919] dark:border-[#E99E05] text-[#191919] dark:text-white font-bold text-sm hover:bg-[#E99E05] hover:text-[#191919] transition" :aria-label="(isAr ? 'اطلب عرض سعر: ' : 'Request a quote: ') + t(m.name)" @click="$emit('request-model', m)">
                  {{ isAr ? 'اطلب عرض سعر' : 'Request a quote' }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Mobile: one card per model -->
      <div class="md:hidden flex flex-col gap-3">
        <article v-for="m in current.models" :key="m.code" :id="anchor(m) + '-m'" class="border border-[#191919] dark:border-gray-600 rounded-xl overflow-hidden">
          <div class="px-4 pt-3 pb-2">
            <h3 class="font-display font-bold text-base text-[#191919] dark:text-white leading-snug">{{ t(m.name) }}</h3>
            <span class="text-xs text-[#5E5F5F] dark:text-gray-400"><bdi>{{ m.code }}</bdi> · {{ t(m.origin) }}</span>
          </div>
          <dl class="grid grid-cols-3 border-t border-[#E4E6E6] dark:border-gray-700">
            <div v-for="k in keyRows" :key="k.key" class="px-2.5 py-2 border-e border-[#E4E6E6] dark:border-gray-700 last:border-e-0">
              <dt class="text-[11px] text-[#5E5F5F] dark:text-gray-400">{{ t(k.label) }}</dt>
              <dd class="text-[13px] font-bold leading-snug text-[#191919] dark:text-white">
                <bdi v-if="has(m, k.key)" :dir="isAr ? 'rtl' : 'ltr'">{{ cell(m, k.key) }}</bdi>
                <span v-else class="font-normal text-[#6F7070]">{{ isAr ? 'عند الطلب' : 'On request' }}</span>
              </dd>
            </div>
          </dl>
          <dl v-if="open[m.code]" class="border-t border-[#E4E6E6] dark:border-gray-700 bg-[#FAFAFA] dark:bg-gray-800">
            <div v-for="row in rowsFor(current)" :key="row.key" class="px-4 py-2 border-b border-[#EEEFEF] dark:border-gray-700">
              <dt class="text-xs text-[#5E5F5F] dark:text-gray-400">{{ t(row.label) }}</dt>
              <dd class="text-sm leading-relaxed text-[#191919] dark:text-gray-200">
                <bdi v-if="has(m, row.key)" :dir="isAr ? 'rtl' : 'ltr'">{{ cell(m, row.key) }}</bdi>
                <span v-else class="text-[#6F7070]">{{ isAr ? 'عند الطلب' : 'On request' }}</span>
              </dd>
            </div>
          </dl>
          <div class="grid grid-cols-2 gap-2 p-3 border-t border-[#E4E6E6] dark:border-gray-700">
            <button type="button" class="min-h-[44px] rounded-lg border border-[#A9AAAA] text-[#191919] dark:text-white text-sm font-bold" :aria-expanded="open[m.code] ? 'true' : 'false'" @click="open[m.code] = !open[m.code]">
              {{ open[m.code] ? (isAr ? 'إخفاء المواصفات' : 'Hide specs') : (isAr ? 'كل المواصفات' : 'All specs') }}
            </button>
            <button type="button" class="min-h-[44px] rounded-lg bg-[#191919] text-white text-sm font-bold" :aria-label="(isAr ? 'اطلب عرض سعر: ' : 'Request a quote: ') + t(m.name)" @click="$emit('request-model', m)">
              {{ isAr ? 'اطلب عرض سعر' : 'Request a quote' }}
            </button>
          </div>
        </article>
        <p class="text-xs text-[#5E5F5F] dark:text-gray-400">{{ t(family.source) }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const props = defineProps({
  family: { type: Object, required: true },
  locale: { type: String, default: 'ar' }
})
defineEmits(['request-model'])

const isAr = computed(() => props.locale === 'ar')
const t = (v) => (v && typeof v === 'object' ? (v[props.locale] || v.ar || '') : (v || ''))
const types = computed(() => props.family.types || [])
const typeId = ref(types.value[0]?.id)
const current = computed(() => types.value.find(x => x.id === typeId.value) || types.value[0])
const open = reactive({})

const has = (m, key) => !!(m.specs && m.specs[key] && t(m.specs[key]))
// Word joiners keep a unit such as "m/s" or "م/ث" on one line.
const cell = (m, key) => t(m.specs[key]).replace(/(م|m)\/(ث|s)/g, '$1⁠/⁠$2')
// A row shows only when at least one model of the type has a value for it.
const rowsFor = (tp) => (props.family.rows || []).filter(r => tp.models.some(m => has(m, r.key)))
const keyRows = computed(() => (props.family.keyRows || []).map(k => (props.family.rows || []).find(r => r.key === k)).filter(Boolean))
const anchor = (m) => `model-${String(m.code).toLowerCase()}`
const countLabel = (n) => isAr.value
  ? (n === 1 ? 'موديل واحد' : n === 2 ? 'موديلان' : `${n} موديلات`)
  : (n === 1 ? '1 model' : `${n} models`)
</script>
