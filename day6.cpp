#include <iostream>

// Good Reference: https://stackoverflow.com/questions/51599273/xor-linked-list-with-c
class Node {
	public:
		Node(int new_data, Node* prev, Node* next): data(new_data), npx(XOR(prev, next)) {}
		Node* XOR(Node* node_a, Node* node_b) {
			return (Node*)(uintptr_t(node_a) ^ uintptr_t(node_b));
		}
		
		Node* getNext(Node* prev) {
			return XOR(prev, npx);
		}

		Node* getPrev(Node* next) {
			return XOR(next, npx);
		}
		int data;
		Node* npx;
};

class LinkedList {
	public:
		Node* XOR(Node* node_a, Node* node_b) {
			return (Node*)(uintptr_t(node_a) ^ uintptr_t(node_b));
		}

		void add(Node* &head, int data) {
			if (head == NULL) {
				head = new Node(data, NULL, NULL);
			} else {
				Node* prev = NULL;
				Node* curr = head;
				Node* next = XOR(prev, curr->npx);

				while (next != NULL) {
					// fast forward the pointer to the end
					prev = curr;
					curr = next;
					next = XOR(prev, curr->npx);
				}

				Node* new_node = new Node(data, curr, NULL);
				curr->npx = XOR(prev, new_node);
			}
			length++;
		}

	int get(int index, Node* head) {
		Node* curr = head;
		Node* prev = NULL;
		while (index && curr) {
			Node* next = XOR(prev, curr->npx);
			prev = curr;
			curr = next;
			index--;
		}
		
		return curr->data;
	}

	void print(Node* &head) {
		unsigned int index = 0;
		while (index < length) {
			std::cout << LinkedList::get(index, head) << std::endl;
			index++;
		}
	}

	unsigned int length = 0;
};

int main()
{
	int array[] = {
		1,
		2,
		3,
		4,
		5
	};
	LinkedList linked_list = LinkedList();
	Node* head = NULL;
	for (int i = 0; i < 5; i++) {
		linked_list.add(head, array[i]);
	}
	linked_list.print(head);
	std::cout << "========================" << std::endl;
	std::cout << linked_list.get(0, head) << std::endl;
	std::cout << linked_list.get(1, head) << std::endl;
	std::cout << linked_list.get(2, head) << std::endl;
	std::cout << linked_list.get(3, head) << std::endl;
	std::cout << linked_list.get(4, head) << std::endl;
	return 0;
}