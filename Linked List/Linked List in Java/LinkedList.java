import java.lang.*;
import java.util.*;

class LinkedList
{
    Node head;
    static class Node
    {
        Node next;
        int data;
        Node(int value)
        {
            data = value;
            next = null;
        }
    }

    static LinkedList insert(LinkedList list, int value)
    {
        Node new_node = new Node(value);
        
        if(list.head == null)
            list.head = new_node;
        else
        {
            Node temp = list.head;
            while(temp.next != null)
                temp = temp.next;
            temp.next = new_node;
        }
        return list;
    }

    static void print(LinkedList list)
    {
        if(list.head == null)
            System.out.println("Linkedlist is Empty!");
        else
        {
            System.out.println("Linked List is:");
            Node temp = list.head;
            while(temp != null)
            {
                System.out.print(temp.data + "->");
                temp = temp.next;
            }
            System.out.print("End");
        }
    }

    public static void main(String args[])
    {
        LinkedList list = new LinkedList();
		list = insert(list, 1); 
		list = insert(list, 2); 
		list = insert(list, 3); 
		list = insert(list, 4); 
		list = insert(list, 5); 
		list = insert(list, 6); 
		list = insert(list, 7); 
		list = insert(list, 8);
        print(list);
    }
}