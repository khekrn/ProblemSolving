package hashtable

// Design a HashMap without using any built-in hash table libraries.

// To be specific, your design should include these functions:

// put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
// get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
// remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

// Example:

// MyHashMap hashMap = new MyHashMap();
// hashMap.put(1, 1);
// hashMap.put(2, 2);
// hashMap.get(1);            // returns 1
// hashMap.get(3);            // returns -1 (not found)
// hashMap.put(2, 1);          // update the existing value
// hashMap.get(2);            // returns 1
// hashMap.remove(2);          // remove the mapping for 2
// hashMap.get(2);            // returns -1 (not found)

// Note:

// All keys and values will be in the range of [0, 1000000].
// The number of operations will be in the range of [1, 10000].
// Please do not use the built-in HashMap library.

// Entry definition
type Entry struct {
	key   int
	value int
	next  *Entry
}

const (
	loadFactor = 0.75
	intMax     = 0x7FFFFFFF
)

func hashFunction(key int, size int) int {
	return (key * intMax) % size
}

// MyHashMap definition
type MyHashMap struct {
	entryList []*Entry
	size      int
	capacity  int
	hashFunc  func(key, size int) int
}

// Constructor function
func Constructor() MyHashMap {
	return MyHashMap{
		entryList: make([]*Entry, 10),
		capacity:  10,
		size:      0,
		hashFunc:  hashFunction,
	}
}

// Put insert key and value to map
func (m *MyHashMap) Put(key int, value int) {
	m.resize()
	index := m.hashFunc(key, m.capacity)
	entry := m.entryList[index]
	if entry == nil {
		m.entryList[index] = &Entry{key: key, value: value}
		m.size++
	} else {
		for entry != nil {
			if entry.key == key {
				entry.value = value
				break
			}
			if entry.next == nil {
				entry.next = &Entry{key: key, value: value}
				m.size++
				break
			}
			entry = entry.next
		}
	}
}

// Get Returns the value to which the specified key is mapped, or -1
func (m *MyHashMap) Get(key int) int {
	index := m.hashFunc(key, m.capacity)
	entry := m.entryList[index]
	for entry != nil {
		if entry.key == key {
			return entry.value
		}
		entry = entry.next
	}
	return -1
}

// Remove removes the mapping of the specified value key if this map contains a mapping for the key
func (m *MyHashMap) Remove(key int) {
	index := m.hashFunc(key, m.capacity)
	entry := m.entryList[index]
	previous := entry
	for entry != nil {
		if entry.key == key {
			if previous == entry {
				m.entryList[index] = entry.next
			} else {
				previous.next = entry.next
			}
			entry = nil
			m.size--
			break
		}
		previous = entry
		entry = entry.next
	}
}

func (m *MyHashMap) resize() {
	if float64(m.size)/float64(m.capacity) > loadFactor {
		newCapacity := m.capacity * 2
		newEntryList := make([]*Entry, newCapacity)
		for _, entry := range m.entryList {
			if entry != nil {
				index := m.hashFunc(entry.key, newCapacity)
				newEntryList[index] = entry
			}
		}
		m.capacity = newCapacity
		m.entryList = newEntryList
	}
}
